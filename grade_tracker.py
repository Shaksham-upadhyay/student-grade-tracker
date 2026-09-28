import json
import os

FILE_NAME = "students.json"


def load_data():
    
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}


def save_data(data):

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def add_student(data):
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in data:
        print("Student already exists.")
        return
    data[name] = {}
    print(f"{name} added successfully.")


def add_marks(data):
    name = input("Enter student name: ").strip()
    if name not in data:
        print("Student not found.")
        return
    subject = input("Enter subject: ").strip()
    try:
        marks = float(input("Enter marks (0-100): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return
    data[name][subject] = marks
    print("Marks saved.")


def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def view_report(data):
    name = input("Enter student name: ").strip()
    if name not in data:
        print("Student not found.")
        return
    subjects = data[name]
    if not subjects:
        print("No marks added yet.")
        return
    print(f"\n--- Report for {name} ---")
    for subject, marks in subjects.items():
        print(f"{subject}: {marks}")
    average = sum(subjects.values()) / len(subjects)
    print(f"Average: {average:.2f}")
    print(f"Grade: {get_grade(average)}\n")


def view_all(data):
    if not data:
        print("No students yet.")
        return
    print("\n--- All Students ---")
    for name, subjects in data.items():
        if subjects:
            avg = sum(subjects.values()) / len(subjects)
            print(f"{name}: Average {avg:.2f} ({get_grade(avg)})")
        else:
            print(f"{name}: No marks yet")
    print()


def main():
    data = load_data()
    while True:
        print("1. Add student")
        print("2. Add marks")
        print("3. View student report")
        print("4. View all students")
        print("5. Save and exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            add_marks(data)
        elif choice == "3":
            view_report(data)
        elif choice == "4":
            view_all(data)
        elif choice == "5":
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()