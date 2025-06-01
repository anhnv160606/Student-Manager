def show_menu():
print("\n========== Student Management System ==========")
print("1. Add a student")
print("2. Display student list")
print("3. Search for a student")
print("4. Update student information")
print("5. Delete a student")
print("6. Show statistics")
print("0. Exit")
print("===============================================")

def get_user_choice():
choice = input("👉 Enter your choice (0–6): ").strip()
return choice