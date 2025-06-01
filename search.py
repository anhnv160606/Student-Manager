from typing import List, Dict

def search_students(students: List[Dict], keyword: str = "", major: str = "", gpa_min: float = 0.0, gpa_max: float = 4.0) -> List[Dict]:
    # Kiểm tra gpa_min và gpa_max hợp lệ
    if gpa_min > gpa_max:
        raise ValueError("gpa_min must be less than or equal to gpa_max")
    
    # Kiểm tra nếu danh sách students rỗng
    if not students:
        return []
    
    results = []
    keyword_lower = keyword.lower()
    major_lower = major.lower()

    for student in students:
        # Kiểm tra xem student có đủ các khóa cần thiết và gpa hợp lệ
        if not all(key in student for key in ["id", "name", "major", "gpa"]):
            continue
        if not isinstance(student["gpa"], (int, float)):
            continue
        if not (0.0 <= student["gpa"] <= 4.0):  # Giả định GPA trong khoảng [0.0, 4.0]
            continue

        # Kiểm tra điều kiện tìm kiếm
        if (
            (keyword_lower in student["id"].lower() or keyword_lower in student["name"].lower())
            and (major_lower in student["major"].lower())
            and (gpa_min <= student["gpa"] <= gpa_max)
        ):
            results.append(student)

    return results