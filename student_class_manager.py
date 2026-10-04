import json
from pathlib import Path

DATA_FILE = Path("students.json")


def load_students():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []


def save_students(students):
    DATA_FILE.write_text(
        json.dumps(students, indent=2),
        encoding="utf-8",
    )


def add_student(students):
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    class_input = input("Classes attended (comma-separated): ").strip()
    classes = [item.strip() for item in class_input.split(",") if item.strip()]

    students.append({"name": name, "classes": classes})
    save_students(students)
    print(f"Added {name}.")


def list_students(students):
    if not students:
        print("No students have been added yet.")
        return

    for student in students:
        classes = ", ".join(student["classes"]) or "No classes listed"
        print(f'{student["name"]}: {classes}')


def main():
    students = load_students()

    while True:
        print("\n1. Add student\n2. List students\n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
