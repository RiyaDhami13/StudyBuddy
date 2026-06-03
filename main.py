import os

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

while True:
  clear_screen()
  print("----Study Buddy----")
  print("--------------------")
  print("1. Add Subjects")
  print("2. View Subjects")
  print("3. Exit")
  print("--------------------")

  choice = int(input("Enter your choice(1-3):").strip())

  if choice == 1:
    input("Enter the subject name:")
  elif choice == 2:
    print("Subjects:")
  elif choice == 3:
    print("Exiting....")
  else:
    input("Invalid choice.Press Enter to continue....")