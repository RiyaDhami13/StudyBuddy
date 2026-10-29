import json
import os
from datetime import datetime
from models import Student, Subject, Task, Goal


# 1. Analytics Engine
def task_completion_rate(student):
    total = len(student.tasks)
    if total == 0:
        return 0.0

    completed = sum(1 for task in student.tasks if task.completed)
    return (completed / total) * 100


def study_hours(student):
    subject_hours = {}

    for session in student.sessions:
        subject = session["subject"]
        hours = session["hours"]
        subject_hours[subject] = subject_hours.get(subject, 0) + hours

    total_hours = sum(subject_hours.values())
    most_studied = (
        max(subject_hours, key=subject_hours.get)
        if subject_hours else None
    )

    return subject_hours, total_hours, most_studied


# 2. Convert Python objects into dictionaries
def to_dict(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

    if isinstance(obj, list):
        return [to_dict(item) for item in obj]

    if isinstance(obj, dict):
        return {key: to_dict(value) for key, value in obj.items()}

    if hasattr(obj, "__dict__"):
        return to_dict(obj.__dict__)

    return obj


# 3. Save student data into JSON (Stored inside data/ directory)
def save_data(student, filepath="data/user_data.json"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    data = to_dict(student)

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


# 4. Load saved student data and re-instantiate the Student object
def load_data(filepath="data/user_data.json"):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
            
            # Reconstruct the Student object from raw dictionary data
            student = Student(name=data.get("name", "Student"))
            
            # Reconstruct subjects
            for sub_data in data.get("subjects", []):
                subject = Subject(
                    sub_data["name"], 
                    sub_data["difficulty"], 
                    sub_data["credit"], 
                    sub_data["target_grade"]
                )
                subject.progress = sub_data.get("progress", 0.0)
                if sub_data.get("created_at"):
                    subject.created_at = datetime.fromisoformat(sub_data["created_at"])
                student.add_subject(subject)
                
            # Reconstruct tasks
            for task_data in data.get("tasks", []):
                deadline = datetime.fromisoformat(task_data["deadline"]) if task_data.get("deadline") else datetime.now()
                task = Task(task_data["title"], deadline, task_data["priority"])
                task.completed = task_data.get("completed", False)
                student.add_task(task)
                
            # Reconstruct goals
            for goal_data in data.get("goals", []):
                goal = Goal(goal_data["target_type"], goal_data["target_hours"])
                goal.achieved_hours = goal_data.get("achieved_hours", 0.0)
                student.add_goal(goal)
                
            # Restore sessions
            student.sessions = data.get("sessions", [])
            
            return student
            
    except FileNotFoundError:
        # If no save file exists yet, return a fresh Student profile
        return Student(name="Riya")


# 5. Display analytics and save data
def display_analytics(student):
    print(
        "Task completion:",
        round(task_completion_rate(student), 2),
        "%"
    )

    subject_hours, total_hours, most_studied = study_hours(student)

    print("Hours per subject:", subject_hours)
    print("Total study hours:", total_hours)
    print("Most studied subject:", most_studied)

    save_data(student)
    print("Student data saved and loaded successfully.")