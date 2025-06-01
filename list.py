import json
from tabulate import tabulate

def list_students(file_path='students.json'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            students = json.load(f)

        if not students:
            print("The student list is empty.")
            return

        table = []
        for student in students:
            table.append([
                student.get("id", ""),
                student.get("name", ""),
                student.get("gender", ""),
                student.get("dob", ""),
                student.get("major", ""),
                student.get("gpa", "")
            ])

        headers = ["ID", "Name", "Gender", "Date of Birth", "Major", "GPA"]
        print(tabulate(table, headers=headers, tablefmt="grid"))

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print("Failed to read data. Please make sure the JSON file is valid.")
    except Exception as e:
        print("Error:", e)