from datetime import datetime 

class Subject:
    def __init__(self, name, difficulty, credit, target_grade):
        self.name = name
        self.difficulty = difficulty 
        self.credit = credit 
        self.progress = 0.0
        self.target_grade = target_grade
        self.created_at = datetime.now()

    def update_progress(self, new_progress):
        # Fixed max/min syntax (max takes 2 arguments)
        self.progress = max(0.0, min(100.0, float(new_progress)))

    def show_info(self):
        """Prints a scannable summary of the subject's status."""
        print(f"Subject: {self.name} ({self.credit} credits)")
        print(f"Difficulty: {self.difficulty}")
        print(f"Target Grade: {self.target_grade}")
        print(f"Current Progress: {self.progress}%")
        print(f"Tracked Since: {self.created_at.strftime('%Y-%m-%d')}")


class Task:
    def __init__(self, title, deadline, priority):
        self.title = title  # Fixed typo (tittle -> title)
        self.deadline = deadline
        self.priority = priority 
        self.completed = False
        self.created_at = datetime.now()

    def mark_task_complete(self):
        self.completed = True 

    def check_overdue(self):
        if not self.completed and datetime.now() > self.deadline:
            return True
        else:
            return False  # Fixed return statement


class Goal:
    def __init__(self, target_type, target_hours):
        self.target_type = target_type
        self.target_hours = target_hours
        self.achieved_hours = 0.0

    def add_study_hours(self, hours):
        if hours > 0:
            self.achieved_hours += hours

    def check_goal_status(self):
        is_reached = self.achieved_hours >= self.target_hours
        remaining = max(0.0, self.target_hours - self.achieved_hours)
        return {
            "target type": self.target_type,
            "target hours": self.target_hours,
            "achieved hours": self.achieved_hours,
            "goal Reached": is_reached,
            "remaining Hours": remaining
        }


class Student:
    def __init__(self, name): 
        self.name = name
        self.subjects = []  # Fixed list type hints
        self.tasks = []     
        self.goals = []     
        self.sessions = []  

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_task(self, task):
        self.tasks.append(task)  # Fixed attribute name (task -> tasks)

    def add_goal(self, goal):
        self.goals.append(goal)  # Fixed attribute name (goal -> goals)

    def log_study_session(self, subject_name, hours, details):
        session_entry = {
            "subject": subject_name,
            "hours": hours,
            "date": datetime.now(),
            "details": details
        }
        self.sessions.append(session_entry)
        
        # Moved inside log_study_session so goals update automatically!
        for goal in self.goals:
            if goal.target_type.lower() in subject_name.lower() or goal.target_type == "general":
                goal.add_study_hours(hours)