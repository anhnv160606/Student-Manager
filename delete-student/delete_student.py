#feature/delete_student.py
import json
import os

STUDENT_FILE = 'students.json'

def load_students():
    if not os.path.exists(STUDENT_FILE):
        return []
    with open(STUDENT_FILE, 'r') as f:
        return json.load(f)

def save_students(students):
    with open(STUDENT_FILE, 'w') as f:
        json.dump(students, f, indent=4, ensure_ascii=False)

def delete_student():
    students = load_students()
    if not students:
        print("Student list is empty.")
        return

    id_to_delete = input("Enter the ID of the student to delete: ").strip()

    for student in students:
        if student.get('id') == id_to_delete:
            print(f"Confirm deletion: {student['name']} (ID: {student['id']})?")
            confirm = input("Type 'yes' to confirm: ").strip().lower()
            if confirm == 'yes':
                students.remove(student)
                save_students(students)
                print("Student has been deleted.")
            else:
                print("Deletion cancelled.")
            break
    else:
        print("Student not found.")

if __name__ == "__main__":
    delete_student()
