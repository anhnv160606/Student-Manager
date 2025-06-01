import json
import os


def load_students(file_path='students.json'):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_students(students, file_path='students.json'):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(students, f, indent=4, ensure_ascii=False)


def add_student(student_data: dict, file_path='students.json'):
    students = load_students(file_path)

   
    if any(student['id'] == student_data['id'] for student in students):
        print(f" Sinh viên với ID {student_data['id']} đã tồn tại.")
        return

    students.append(student_data)
    save_students(students, file_path)
    print(f" Đã thêm sinh viên {student_data['name']} (ID: {student_data['id']}) thành công.")

# Chạy hàm nếu gọi trực tiếp file này
if __name__ == '__main__':
    student = {
        'id': input("Nhập ID: "),
        'name': input("Nhập tên: "),
        'gender': input("Nhập giới tính: "),
        'dob': input("Nhập ngày sinh (YYYY-MM-DD): "),
        'major': input("Nhập chuyên ngành: "),
        'gpa': float(input("Nhập GPA: "))
    }

    add_student(student)
