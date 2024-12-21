# main.py
import register
import attendance
import attendance_to_excel

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Register a new user")
        print("2. Start face recognition")
        print("3. Generate Attendance Excel Sheet")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            register.register_user()
        elif choice == "2":
            attendance.recognize_faces()
        elif choice == "3":
            attendance_to_excel.convert_csv_to_excel()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
