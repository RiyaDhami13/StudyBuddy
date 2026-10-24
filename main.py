import sys

#from models import Student, Subjects, Tasks, Goal
#from utils import Validator, StudySession
#from analytics import Analytics
#from storage import save_data, load_data

class StudyBuddyApp:                                                      #Master Controller class
    """Main controller class that coordinates the entire application."""

    def __init__(self):
        self.student = None                     #Main student object will be held here

    def initialize_app(self):     
        """Startup sequence: Load student data from storage or create profile."""
        print("Initializing StudyBuddy...")
        # TODO: Load student data using storage logic
        # self.student = load_data()
        # Temporary placeholder instantiation until storage is hooked up:
        # self.student = Student(name="Riya", semester="1st")
        print("Welcome Back, Student!")

    def print_banner(self):
        """Prints a clean ASCII banner for StudyBuddy."""
        print("=" * 50)
        print("              STUDYBUDDY  2.0(CLI EDITION)                 ")
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
            choice = input("Enter your choice(1-6):").strip()

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
                print("\n[Error] Invalid choice ! Please enter a number between 1 and 6.")
                input("Press Enter to try again....")

    def handle_subjects_menu(self):
        """Handles subject addition and info viewing."""
        print("\n--- SUBJECT MANAGEMENT ---")
        print("1. Add a Subject (Calls Student.add_subjects)")
        print("2. View Subject Info (Calls Subject.show_info)")
        sub_choice = input("Select options or press Enter to return:").strip()
        # TODO: Hook up Subjects from models.py
        input("\n Press Enter to return to main menu.")

    def handle_dashboard_menu(self):
        """Handles viewing analytics, completion rates, and dashboards."""
        print("\n--- DASHBOARD ANALYTICS ---")
        print("1. Show Dashboard (Calls Student.show_dashboard)")
        print("2. Completion Rate (Calls Analytics.completion_rate)")
        print("3. Most Studied Subject (Calls Analytics.most_studied_subject)")
        #TODO: Hookup Analytics class methods
        input("\nPress Enter to return to main menu....")

    def handle_goals_menu(self):
        """Handles weekly and semester target study goals."""
        print("\n--- GOALS MANAGEMENT ---")
        print("1. Check Goal Status (Calls Goal.check_goal_status)")
        print("2. Update Target Hours(Calls Goal.update_target)")
        input("\nPress Enter to return to main menu....")

    def print_exit_sequence(self):
        """Saves data to JSON storage and exits."""
        print("\nSaving data to storage....Goodbye!")
        #TODO: Connect with storage module to serialize and save data via JSON

if __name__ == "__main__":
    app = StudyBuddyApp()
    app.run()

    
        
