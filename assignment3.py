def load_students(filename):
    students = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                if line:  
                    studentId, lastName, firstName, major, gpa = line.split(",")
                    students[studentId] = [lastName, firstName, major, gpa]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return students


def search_by_lastname(students, lname):
    return {sid: data for sid, data in students.items() if data[0].lower() == lname.lower()}


def search_by_major(students, major):
    return {sid: data for sid, data in students.items() if data[2].lower() == major.lower()}


def print_students(students):
    if not students:
        print("No matching students found.\n")
        return
    for sid, data in students.items():
        lastName, firstName, major, gpa = data
        print(f"\nID: {sid}, Last Name: {lastName}, First Name: {firstName}, Major: {major}, GPA: {gpa}")
    print()


def main():
    filename = "C:/Users/jleen/CS222/assignments/students.txt"
    students = load_students(filename)
    if not students:
        return  

    while True:
        print("Choose an option:")
        print("1) Search by Last Name")
        print("2) Search by Major")
        print("3) Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            lname = input("Enter last name to search for: ")
            results = search_by_lastname(students, lname)
            print_students(results)
        elif choice == "2":
            major = input("Enter major to search for: ")
            results = search_by_major(students, major)
            print_students(results)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
