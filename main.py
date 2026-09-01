import os

class StudyBuddyApp:
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')  

    def __init__(self):
        # The list belongs directly to this app instance
        self.subjects = []

    def add_subjects(self, name, difficulty):
        """Adds a subject name and difficulty level."""
        subject = {
            "name": name,
            "difficulty": difficulty
        }
        self.subjects.append(subject)
        print(f"\nSuccessfully added {name}!")

    def view_subjects(self):
        """Displays all subjects."""
        if not self.subjects:
            print("\nNo subjects added yet.")
            return
        
        print("\nSubjects are:")
        for index, item in enumerate(self.subjects, start=1):
            # We use 'item' (the dictionary), NOT 'index' (the number)
            print(f"{index}. {item.get('name')} (Difficulty level: {item.get('difficulty')})")

    def run(self):
        while True:
            self.clear_screen()
            print("----Study Buddy----")
            print("--------------------")
            print("1. Add Subjects")
            print("2. View Subjects")
            print("3. Exit")
            print("--------------------")

            try:
                choice = int(input("Enter your choice(1-3): ").strip())
            except ValueError:
                input("\nPlease enter a valid number. Press Enter to continue...")
                continue

            if choice == 1:
                name = input("Enter the subject name: ")
                difficulty = input("Enter the difficulty level: ")
                self.add_subjects(name, difficulty)
                input("\nPress Enter to Continue...")
            
            elif choice == 2:
                self.view_subjects()
                input("\nPress Enter to Continue...")

            elif choice == 3:
                print("\nExiting......")
                break
            
            else:
                input("\nInvalid choice. Press Enter to continue...")

# Create and start the application engine
if __name__ == "__main__":
    app = StudyBuddyApp()
    app.run()