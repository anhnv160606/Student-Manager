import json

STUDENT_FILE = 'students.json'

def load_students() -> list:
    try:
        with open(STUDENT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ Lỗi định dạng file JSON.")
        return []

def save_students(data: list):
    with open(STUDENT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_student_by_id(student_id: str, updated_data: dict) -> bool:
    students = load_students()
    found = False

    for student in students:
        if student.get("id") == student_id:
            student.update(updated_data)
            found = True
            break

    if found:
        save_students(students)
        print(f"✅ Student with ID {student_id} updated successfully.")
    else:
        print(f"❌ Student with ID {student_id} not found.")

    return found
