# Members:
# ALVAREZ, MARK JOSEPH A. - Menu, Add Student, Validation
# BASILA, ASHLEY D. - View, Search, Delete

# Lists to store student information
names = []
ages = []

# Function to show menu
def menu():
    print("\n=== STUDENT INFORMATION SYSTEM ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

# Function to add a student
def add_student():
    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return

    age_input = input("Enter student age: ")
    if not age_input.isdigit():
        print("Age must be a number.")
        return

    age = int(age_input)
    if age <= 0:
        print("Age must be more than 0.")
        return

    names.append(name)
    ages.append(age)
    print(f"Student '{name}' is added.")

#Placeholder functions for my duo (Ashley Basila)
def view_students():
    print("This part is not ready yet.")

def search_student():
    print("This part is not ready yet.")

def delete_student():
    print("This part is not ready yet.")

# Main program loop
while True:
    menu()
    choice = input("Choose an option (1-5) only :) : ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program. Bye!")
        break
    else:
        print("Wrong choice. Enter number 1 to 5.")
