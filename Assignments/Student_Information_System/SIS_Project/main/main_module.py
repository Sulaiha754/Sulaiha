from dao.sisrepo_impl import SISRepoImpl
from entity.student import Student
from entity.enrollment import Enrollment
from entity.payment import Payment

def main():
    repo = SISRepoImpl()

    while True:
        print("\n--- Student Information System ---")
        print("1. Add Student\n2. Enroll Student\n3. Assign Teacher\n4. Make Payment\n5. Enrollment Report\n6. View All Courses\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
                print("Enter Student Details:")
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                dob = input("Date of Birth (YYYY-MM-DD): ")
                email = input("Email: ")
                phone = input("Phone Number: ")

                student = Student(None, first_name, last_name, dob, email, phone)
                student_id = repo.insert_student(student)
                print("Student added successfully.")
                print(f"Student ID: {student_id}")

        elif choice == "2":
            sid = int(input("Enter Student ID to enroll: "))
            cid = int(input("Enter Course ID: "))
            edate = input("Enter Enrollment Date (YYYY-MM-DD): ")
            enrollment = Enrollment(None, sid, cid, edate)
            repo.enroll_student(enrollment)
            print("Student enrolled.")


        elif choice == "3":
            repo.assign_teacher(301, 401)
            print("Teacher assigned.")

        elif choice == "4":
            sid = int(input("Enter Student ID for payment: "))
            amount = float(input("Enter Payment Amount: "))
            pdate = input("Enter Payment Date (YYYY-MM-DD): ")
            payment = Payment(None, sid, amount, pdate)
            repo.make_payment(payment)
            print("Payment recorded.")


        elif choice == "5":
            cname = input("Enter Course Name to generate report: ")
            report = repo.generate_enrollment_report(cname)
            if report:
                for r in report:
                    print(f"Student: {r[0]} {r[1]} | Enrollment Date: {r[2]}")
            else:
                print("No enrollments found for this course.")

        elif choice == "6":
            courses = repo.get_all_courses()
            if courses:
                print("\n--- Available Courses ---")
                for c in courses:
                        print(f"ID: {c[0]} | Name: {c[1]} | Credits: {c[2]} | Teacher ID: {c[3]}")
            else:
                 print("No courses found.")

        elif choice == "7":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
