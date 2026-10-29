import sys
from datetime import datetime
from models import Student, Subject, Task, Goal
#from utils import Validator, StudySession
from analytics import load_data, save_data, display_analytics
#from storage import save_data, load_data

class StudyBuddyApp:
    """Main controller class that coordinates the entire application."""

    def __init__(self):
        self.student = None  # Main student object will be held here

    def initialize_app(self): 
        """Startup sequence: Load student data from storage or create profile."""
        print("Initializing StudyBuddy...")
        #  Load student data using team mate 3's logic later
        self.student = load_data()

        print(f"Welcome back, {self.student.name}")
        
        # Instantiate a live Student object for now:
        #print("Welcome Back, Student!")

    def print_banner(self):
        """Prints a clean ASCII banner for StudyBuddy."""
        print("=" * 50)
        print("               STUDYBUDDY  2.0 (CLI EDITION)                ")
        print("=" * 50)

    def run(self):
        """Main execution loop showing the menu and handling user routing."""
        self.initialize_app()

        while True:
            self.print_banner()
            print("1. Manage Subjects")
            print("2. Manage Tasks & Deadlines")
            print("3. Log Study Session")
            print("4. View Dashboard & Stats")
            print("5. Manage Goals")
            print("6. Save & Exit")
            print("=" * 50)

            # TODO: Use Validator class here to safely capture integer choices
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.handle_subjects_menu()
            elif choice == "2":
                self.handle_tasks_menu()
            elif choice == "3":
                self.handle_study_session_menu()
            elif choice == "4":
                self.handle_dashboard_menu()
            elif choice == "5":
                self.handle_goals_menu()
            elif choice == "6":
                self.print_exit_sequence()
                break
            else:
                print("\n[Error] Invalid choice! Please enter a number between 1 and 6.")
                input("Press Enter to try again....")

    def handle_subjects_menu(self):
        """Handles subject addition and info viewing using Teammate 1's Subject class."""
        while True:
            print("\n--- SUBJECT MANAGEMENT ---")
            print("1. Add a Subject")
            print("2. View Subject Info")
            print("3. Return to Main Menu")
            sub_choice = input("Select option (1-3): ").strip()

            if sub_choice == "1":
                name = input("Enter subject name: ").strip()
                difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip()
                credit = int(input("Enter credit hours: ").strip())
                target_grade = input("Enter target grade (e.g. A): ").strip()

                new_subject = Subject(name, difficulty, credit, target_grade)
                self.student.add_subject(new_subject)
                print(f"\n[Success] Subject '{name}' added successfully!")
                input("\nPress Enter to continue...")

            elif sub_choice == "2":
                if self.student.subjects:
                    print("\n--- YOUR SUBJECTS ---")
                    for sub in self.student.subjects:
                        sub.show_info()
                        print("-" * 30)
                else:
                    print("\n[Notice] No subjects found yet.")
                input("\nPress Enter to continue...")

            elif sub_choice == "3":
                break
            else:
                print("\n[Error] Invalid choice.")
                input("Press Enter to try again...")

    def handle_tasks_menu(self):
        """Handles task creation and viewing using Teammate 1's Task class."""
        while True:
            print("\n--- TASK & DEADLINE MANAGEMENT ---")
            print("1. Add a Task")
            print("2. View All Tasks")
            print("3. Return to Main Menu")
            sub_choice = input("Select option (1-3): ").strip()

            if sub_choice == "1":
                title = input("Enter task title: ").strip()
                deadline_str = input("Enter deadline (YYYY-MM-DD): ").strip()
                priority = input("Enter priority (Low/Medium/High): ").strip()

                try:
                    deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
                    new_task = Task(title, deadline, priority)
                    self.student.add_task(new_task)
                    print(f"\n[Success] Task '{title}' added!")
                except ValueError:
                    print("\n[Error] Invalid date format. Please use YYYY-MM-DD.")
                input("\nPress Enter to continue...")

            elif sub_choice == "2":
                if self.student.tasks:
                    print("\n--- YOUR TASKS ---")
                    for i, task in enumerate(self.student.tasks, 1):
                        status = "Completed" if task.completed else "Pending"
                        print(f"{i}. {task.title} | Priority: {task.priority} | Status: {status} | Deadline: {task.deadline.strftime('%Y-%m-%d')}")
                else:
                    print("\n[Notice] No tasks recorded yet.")
                input("\nPress Enter to continue...")

            elif sub_choice == "3":
                break
            else:
                print("\n[Error] Invalid choice.")
                input("Press Enter to try again...")

    def handle_dashboard_menu(self):
        """Handles viewing analytics and student overview."""
        #  Hooked up Analytics class methods from Teammate 3 later
        display_analytics(self.student)
        input("\nPress Enter to return to main menu....")

    def handle_goals_menu(self):
        """Handles weekly and semester target study goals using Teammate 1's Goal class."""
        while True:
            print("\n--- GOALS MANAGEMENT ---")
            print("1. Add a Goal")
            print("2. Check Goal Status")
            print("3. Return to Main Menu")
            sub_choice = input("Select option (1-3) : ").strip()

            if sub_choice == "1":
                target_type = input("Enter goal type (e.g. 'General' or subject name): ").strip()
                target_hours = float(input("Enter target study hours: ").strip())
                new_goal = Goal(target_type, target_hours)
                self.student.add_goal(new_goal)
                print(f"\n[Success] Goal for '{target_type}' ({target_hours} hrs) added!")
                input("\nPress Enter to continue...")

            elif sub_choice == "2":
                if self.student.goals:
                    print("\n--- GOAL STATUS ---")
                    for goal in self.student.goals:
                        status = goal.check_goal_status()
                        print(f"Target: {status['target type']} | Target Hours: {status['target hours']} | Achieved: {status['achieved hours']} hrs | Reached: {status['goal Reached']}")
                else:
                    print("\n[Notice] No goals set yet.")
                input("\nPress Enter to continue...")

            elif sub_choice == "3":
                break
            else:
                print("\n[Error] Invalid choice.")
                input("Press Enter to try again...")

    def handle_study_session_menu(self):
        """Placeholder for study logging."""
        print("\n--- STUDY SESSION LOGGER ---")
        print("Study session logging will be fully linked when Teammate 2's StudySession is ready.")
        input("\nPress Enter to return to main menu...")

    def print_exit_sequence(self):
        """Saves data to JSON storage and exits."""
        print("\nSaving data to storage....Goodbye!")
        # Connected with storage module to serialize and save data via JSON
        save_data(self.student)
        print("Data saved sucessfully. BYE BYE !")

if __name__ == "__main__":
    app = StudyBuddyApp()
    app.run()