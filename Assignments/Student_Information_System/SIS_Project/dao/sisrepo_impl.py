import pyodbc
from util.db_conn_util import DBConnUtil

class SISRepoImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def insert_student(self, student):
        query = "INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number) OUTPUT INSERTED.student_id VALUES (?, ?, ?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(query, (student.first_name, student.last_name, student.dob, student.email, student.phone))
        student_id = cursor.fetchone()[0]
        self.conn.commit()
        return student_id


    def enroll_student(self, enrollment):
        query = "INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(query, (enrollment.student_id, enrollment.course_id, enrollment.enrollment_date))
        self.conn.commit()

    def assign_teacher(self, course_id, teacher_id):
        query = "UPDATE Courses SET teacher_id = ? WHERE course_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (teacher_id, course_id))
        self.conn.commit()

    def make_payment(self, payment):
        query = "INSERT INTO Payments (student_id, amount, payment_date) VALUES (?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(query, (payment.student_id, payment.amount, payment.payment_date))
        self.conn.commit()

    def get_all_courses(self):
        query = "SELECT course_id, course_name, credits, teacher_id FROM Courses"
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def generate_enrollment_report(self, course_name):
        query = (
            "SELECT s.first_name, s.last_name, e.enrollment_date "
            "FROM Enrollments e "
            "JOIN Students s ON e.student_id = s.student_id "
            "JOIN Courses c ON e.course_id = c.course_id "
            "WHERE c.course_name = ?"
        )
        cursor = self.conn.cursor()
        cursor.execute(query, (course_name,))
        return cursor.fetchall()
