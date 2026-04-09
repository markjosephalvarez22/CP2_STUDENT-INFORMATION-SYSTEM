def view_students():
    if len(names) == 0:
        print("No students to display.")
    else:
        print("\n--- STUDENT LIST ---")
        for i in range(len(names)):
            print(f"{i+1}. Name: {names[i]}, Age: {ages[i]}")

def search_student():
    search_name = input("Enter name to search: ").strip()
    found = False
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print(f"Found: {names[i]}, Age: {ages[i]}")
            found = True
            break
    if not found:
        print("Student not found.")

def delete_student():
    del_name = input("Enter name to delete: ").strip()
    found = False
    for i in range(len(names)):
        if names[i].lower() == del_name.lower():
            confirm = input(f"Are you sure you want to delete {names[i]}? (y/n): ")
            if confirm.lower() == "y":
                names.pop(i)
                ages.pop(i)
                print("Student deleted successfully.")
            else:
                print("Delete cancelled.")
            found = True
            break
    if not found:
        print("Student not found.")
