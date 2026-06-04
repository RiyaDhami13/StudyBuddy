import os

class StudyBuddyApp:
  def clear_screen(self):
    os.system('cls' if os.name == 'nt' else 'clear')  

  def __init__(self):      #object sets up its own internal data
    # the list will now belong to this APP.
    self.subjects = []
  

#this is the first method i made
  def add_subjects(self,name,difficulty):
      """Add your Subject name and difficulty level.
      """

      #Formlating the records of subjects
      subject = {
      "name":name,
      "difficulty":difficulty
    }
      
    #Storing them into the list
      self.subjects.append(subject)
      print(f"Successfully added {name}")

#this is a method to view subjects
  def view_subjects(self):
    """Displays all subjects."""
    if not self.subjects:
      print("\n No subjects added yet.")
      return
    
    print("Subjects are:")
    for index,item in enumerate(self.subjects,start = 1):
      print(f"{index}. {item[name]} (Difficulty level:{item[difficulty]})")



#Object(app) is created from blueprint(StudyBuddyApp)
app = StudyBuddyApp()

#app runs its method now
app.clear_screen()
print("Screen clear")

while True:
  app.clear_screen()
  print("----Study Buddy----")
  print("--------------------")
  print("1. Add Subjects")
  print("2. View Subjects")
  print("3. Exit")
  print("--------------------")

  choice = int(input("Enter your choice(1-3):").strip())

  if choice == 1:
    name = input("Enter the subject name:")
    difficulty = input("Enter the difficulty level")
    app.add_subjects(name,difficulty)

    
  elif choice == 2:
    app.view_subjects()

  elif choice == 3:
    print("Exiting....")
    break   
  else:
    input("Invalid choice.Press Enter to continue....")

