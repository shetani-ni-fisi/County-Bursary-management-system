class Student:
    def __init__(self, student_id, name, bursary_status=False):
        self.student_id = student_id
        self.name = name
        self.bursary_status = bursary_status

    def update_bursary_status(self, status):
        self.bursary_status = status

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Bursary Status: {'Granted' if self.bursary_status else 'Not Granted'}"


class BursaryManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully.")

    def update_bursary_status(self, student_id, status):
        if student_id in self.students:
            self.students[student_id].update_bursary_status(status)
            print(f"Bursary status for student ID {student_id} updated to {'Granted' if status else 'Not Granted'}.")
        else:
            print(f"Student with ID {student_id} not found.")

    def view_student(self, student_id):
        if student_id in self.students:
            print(self.students[student_id])
        else:
            print(f"Student with ID {student_id} not found.")

    def view_all_students(self):
        for student in self.students.values():
            print(student)


def main():
    system = BursaryManagementSystem()

    while True:
        print("\nBursary Management System")
        print("1. Add Student")
        print("2. Update Bursary Status")
        print("3. View Student Details")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            system.add_student(student_id, name)
        elif choice == '2':
            student_id = input("Enter Student ID: ")
            status = input("Enter Bursary Status (Granted/Not Granted): ").lower() == 'granted'
            system.update_bursary_status(student_id, status)
        elif choice == '3':
            student_id = input("Enter Student ID: ")
            system.view_student(student_id)
        elif choice == '4':
            system.view_all_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()