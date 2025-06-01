import menu
import add
import list
import search
import update
import delete_student

def main():

    while True:
        menu.show_menu()
        choice = menu.get_user_choice()

        if choice == "1":
            student = {
                'id': input("Nhập ID: "),
                'name': input("Nhập tên: "),
                'gender': input("Nhập giới tính: "),
                'dob': input("Nhập ngày sinh (YYYY-MM-DD): "),
                'major': input("Nhập chuyên ngành: "),
                'gpa': float(input("Nhập GPA: "))
            }
            add.add_student(student)

        elif choice == "2":
            list.list_students()
        elif choice == "3":
            students = add.load_students()

            if not students:
                print("Không có dữ liệu sinh viên để tìm kiếm.")
                return

            print("\n--- TÌM KIẾM SINH VIÊN ---")
            keyword = input("Nhập từ khóa (ID hoặc tên): ").strip()
            major = input("Nhập chuyên ngành (có thể để trống): ").strip()

            try:
                gpa_min = float(input("Nhập GPA tối thiểu (mặc định 0.0): ").strip() or 0.0)
                gpa_max = float(input("Nhập GPA tối đa (mặc định 4.0): ").strip() or 4.0)
            except ValueError:
                print("Lỗi: GPA phải là số.")
                return

            if gpa_min > gpa_max:
                print("Lỗi: GPA tối thiểu không được lớn hơn GPA tối đa.")
                return

            results = search.search_students(students, keyword, major, gpa_min, gpa_max)

            if results:
                print(f"\nĐã tìm thấy {len(results)} sinh viên:")
                for student in results:
                    print(
                        f"- ID: {student['id']} | Tên: {student['name']} | Giới tính: {student.get('gender', 'N/A')} | "
                        f"Ngày sinh: {student.get('dob', 'N/A')} | Chuyên ngành: {student['major']} | GPA: {student['gpa']}")
            else:
                print("Không tìm thấy sinh viên nào phù hợp.")



        elif choice == "4":
        

                if choice == "4":  # Giả sử 4 là chọn cập nhật
                    student_id = input("Nhập ID sinh viên cần cập nhật: ").strip()
                    updated_data = {}

                    name = input("Tên mới (Enter để bỏ qua): ").strip()
                    gender = input("Giới tính mới (Enter để bỏ qua): ").strip()
                    dob = input("Ngày sinh mới (Enter để bỏ qua): ").strip()
                    major = input("Chuyên ngành mới (Enter để bỏ qua): ").strip()
                    gpa_str = input("GPA mới (Enter để bỏ qua): ").strip()

                    if name:
                        updated_data['name'] = name
                    if gender:
                        updated_data['gender'] = gender
                    if dob:
                        updated_data['dob'] = dob
                    if major:
                        updated_data['major'] = major
                    if gpa_str:
                        try:
                            updated_data['gpa'] = float(gpa_str)
                        except ValueError:
                            print("GPA không hợp lệ. Bỏ qua cập nhật GPA.")

                    if updated_data:
                        update.update_student_by_id(student_id, updated_data)
                    else:
                        print("Không có dữ liệu để cập nhật.")

                # ... các lựa chọn khác ...

        elif choice == "5":
            delete_student.delete_student()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

