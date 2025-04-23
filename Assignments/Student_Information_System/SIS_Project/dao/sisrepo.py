from abc import ABC, abstractmethod

class SISRepo(ABC):
    @abstractmethod
    def insert_student(self, student): pass

    @abstractmethod
    def enroll_student(self, enrollment): pass

    @abstractmethod
    def assign_teacher(self, course_id, teacher_id): pass

    @abstractmethod
    def make_payment(self, payment): pass

    @abstractmethod
    def generate_enrollment_report(self, course_name): pass
