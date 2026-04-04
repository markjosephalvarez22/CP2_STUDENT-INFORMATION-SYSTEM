# Members:
# ALVAREZ, MARK JOSEPH A. - Menu, Add Student, Validation
# BASILA, ASHLEY D. - View, Search, Delete

names = []
ages = []

def menu():
    print("\n=== STUDENT INFORMATION SYSTEM ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
while True:
    menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice in ["1", "2", "3", "4", "5"]:
        print(f"You selected option {choice}")
        if choice == "5":
            print("Exiting...")
            break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
