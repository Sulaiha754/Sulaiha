------------------------------------------------------------------ASSIGNMENT 2-----------------------------------------------------------------------------------------------

-----------------------------------------------------------------TASK 1 -----------------------------------------------------------------------------------------------------------

-- 1. Create Database
CREATE DATABASE SISDB;

-- 2. Use Database
USE SISDB;

-- a. Students Table
CREATE TABLE Students (student_id INT PRIMARY KEY IDENTITY(1,1),first_name VARCHAR(50),last_name VARCHAR(50),date_of_birth DATE,email VARCHAR(100),phone_number VARCHAR(15));

-- b. Teacher Table
CREATE TABLE Teacher (teacher_id INT PRIMARY KEY IDENTITY(1,1),first_name VARCHAR(50),last_name VARCHAR(50),email VARCHAR(100));

-- c. Courses Table
CREATE TABLE Courses (course_id INT PRIMARY KEY IDENTITY(1,1),course_name VARCHAR(100),credits INT,teacher_id INT, FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id));

-- d. Enrollments Table
CREATE TABLE Enrollments (enrollment_id INT PRIMARY KEY IDENTITY(1,1),student_id INT,course_id INT,enrollment_date DATE,FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id));

-- e. Payments Table
CREATE TABLE Payments (payment_id INT PRIMARY KEY IDENTITY(1,1),student_id INT,amount DECIMAL(10, 2), payment_date DATE,
FOREIGN KEY (student_id) REFERENCES Students(student_id));

insert into students (first_name, last_name, date_of_birth, email, phone_number) values('Anisha', 'parveen', '2010-12-18', 'anish@yahoo.com', '1234567800'),
('roshni', 'maran', '2019-01-27', 'roshni@yahoo.com', '1234567801'),
('divya', 'durga', '2021-08-21', 'divya@gmail.com', '1234567802'),('ubasana', 'pooja', '2021-09-28', 'ubas@example.com', '1234567803'),
('taruna', 'ravi', '2016-06-06', 'taruna@example.com', '1234567804'),('aruna', 'darshini', '2012-11-13', 'aruna@example.com', '1234567805'),
('Daniel', 'Lee', '2014-03-22', 'daniel.lee@example.com', '1234567806'),
('Grace', 'Clark', '2017-07-07', 'grace.clark@example.com', '1234567807'),('Henry', 'Lewis', '2013-10-30', 'henry.lewis@example.com', '1234567808'),
('Sophia', 'Hall', '2018-05-17', 'sophia.hall@example.com', '1234567809');

select * from students;

insert into teacher (first_name, last_name, email) values('Alan', 'Turing', 'alan.turing@example.com'),('Ada', 'Lovelace', 'ada.lovelace@example.com'),
('Grace', 'Hopper', 'grace.hopper@example.com'),('Linus', 'Torvalds', 'linus.torvalds@example.com'),('Tim', 'Berners-Lee', 'tim.berners@example.com'),
('James', 'Gosling', 'james.gosling@example.com'),('Dennis', 'Ritchie', 'dennis.ritchie@example.com'),
('Guido', 'van Rossum', 'guido.rossum@example.com'),('Barbara', 'Liskov', 'barbara.liskov@example.com'),
('Donald', 'Knuth', 'donald.knuth@example.com');

select * from teacher;

insert into courses (course_name, credits, teacher_id) values('Mathematics', 4, 1),('Computer Science', 3, 2),('Physics', 4, 3),('Chemistry', 3, 4),('Biology', 3, 5),
('English Literature', 2, 6),('History', 3, 7),('Geography', 2, 8),('Philosophy', 3, 9),('Art', 2, 10);

select * from courses;

insert into enrollments (student_id, course_id, enrollment_date) values(1, 1, '2024-01-15'),(1, 2, '2024-01-16'),(2, 3, '2024-02-10'),(3, 1, '2024-02-12'),(4, 4, '2024-03-01'),
(5, 5, '2024-03-15'),(6, 6, '2024-03-20'),(7, 7, '2024-04-01'),(8, 8, '2024-04-05'),(9, 9, '2024-04-10');

select * from enrollments;

insert into payments (student_id, amount, payment_date) values(1, 5000, '2024-01-20'),(2, 3000, '2024-02-15'),(3, 4000, '2024-02-20'),(4, 2500, '2024-03-05'),
(5, 3500, '2024-03-18'),(6, 2000, '2024-03-25'),(7, 4500, '2024-04-02'),(8, 3000, '2024-04-07'),(9, 2800, '2024-04-12'),(10, 3300, '2024-04-18');

select * from payments;

-------------------------------------------------------------------------TASK 2-----------------------------------------------------------------------------------------------------------

--1. Write an SQL query to insert a new student into the "Students" table with the following details:a. First Name: John b. Last Name: Doe c. Date of Birth: 1995-08-15
--d. Email: john.doe@example.com, e. Phone Number: 1234567890

insert into students (first_name, last_name, date_of_birth, email, phone_number)values ('John', 'Doe', '1995-08-15', 'john.doe@example.com', '1234567890');

--2.  Write an SQL query to enroll a student in a course. Choose an existing student and course and insert a record into the "Enrollments" table with the enrollment date

insert into enrollments (student_id, course_id, enrollment_date)values (1, 2, '2025-04-23');

--3.Update the email address of a specific teacher in the "Teacher" table. Choose any teacher and modify their email address

update teacher set email = 'turing.tur@example.com' where teacher_id = 1;

--4. . Write an SQL query to delete a specific enrollment record from the "Enrollments" table. Select an enrollment record based on the student and course

delete from enrollments where student_id = 1 and course_id = 2;

--5. Update the "Courses" table to assign a specific teacher to a course. Choose any course and teacher from the respective tables

update courses set teacher_id = 5 where course_id = 3;

--6. Delete a specific student from the "Students" table and remove all their enrollment records from the "Enrollments" table. Be sure to maintain referential integrity

delete from enrollments where student_id = 10;
delete from students where student_id = 10;

--7. Update the payment amount for a specific payment record in the "Payments" table. Choose any payment record and modify the payment amount.

update payments set amount = 4500 where payment_id = 3;

----------------------------------------------------------------TASK 3------------------------------------------------------------------------------------------------------------------

--1. Write an SQL query to calculate the total payments made by a specific student. You will need to join the "Payments" table with the "Students" table based on the student's ID.

select s.student_id, s.first_name, s.last_name, sum(p.amount) as total_payments from students s join payments p on s.student_id = p.student_id
where s.student_id = 1  group by s.student_id, s.first_name, s.last_name;

--2. Write an SQL query to retrieve a list of courses along with the count of students enrolled in each course. Use a JOIN operation between the "Courses" table and the "Enrollments" table.

select c.course_id, c.course_name, count(e.student_id) as student_count from courses c join enrollments e on c.course_id = e.course_id group by c.course_id, c.course_name;

--3. Write an SQL query to find the names of students who have not enrolled in any course. Use a LEFT JOIN between the "Students" table and the "Enrollments" table to identify students without enrollments.

select s.student_id, s.first_name, s.last_name from students s left join enrollments e on s.student_id = e.student_id where e.enrollment_id is null;

--4. Write an SQL query to retrieve the first name, last name of students, and the names of the courses they are enrolled in. Use JOIN operations between the "Students" table and the "Enrollments" and "Courses" tables.

select  s.first_name,s.last_name,c.course_name from students s inner join enrollments e on s.student_id = e.student_id inner join courses c on e.course_id = c.course_id;

--5. Create a query to list the names of teachers and the courses they are assigned to. Join the "Teacher" table with the "Courses" table.

select t.first_name,t.last_name,c.course_name from teacher t inner join courses c on t.teacher_id = c.teacher_id;

--6. Retrieve a list of students and their enrollment dates for a specific course. You'll need to join the "Students" table with the "Enrollments" and "Courses" tables.

select  s.first_name, s.last_name, c.course_name,e.enrollment_date from students s inner join enrollments e on s.student_id = e.student_id inner join courses c 
on e.course_id = c.course_id  where c.course_name = 'Mathematics';

--7. Find the names of students who have not made any payments. Use a LEFT JOIN between the "Students" table and the "Payments" table and filter for students with NULL payment records.

select  s.first_name, s.last_name from students s left join payments p on s.student_id = p.student_id where p.payment_id is null;

--8. . Write a query to identify courses that have no enrollments. You'll need to use a LEFT JOIN between the "Courses" table and the "Enrollments" table and filter for courses with NULL enrollment records.

select  c.course_id, c.course_name from courses c left join enrollments e on c.course_id = e.course_id where e.enrollment_id is null;

--9. Identify students who are enrolled in more than one course. Use a self-join on the "Enrollments" table to find students with multiple enrollment records.

select s.student_id, s.first_name, s.last_name, count(e.course_id) as course_count from students s join enrollments e on s.student_id = e.student_id
group by s.student_id, s.first_name, s.last_name having count(e.course_id) > 1;

--10. Find teachers who are not assigned to any courses. Use a LEFT JOIN between the "Teacher" table and the "Courses" table and filter for teachers with NULL course assignments.

SELECT t.* FROM Teacher t LEFT JOIN Courses c ON t.teacher_id = c.teacher_id WHERE c.course_id IS NULL;

--------------------------------------------------------------------------------TASK 4 ---------------------------------------------------------------------------------------------------

--1. Write an SQL query to calculate the average number of students enrolled in each course. Use aggregate functions and subqueries to achieve this.

SELECT c.course_name,  (SELECT COUNT(*) FROM Enrollments e WHERE e.course_id = c.course_id) AS avg_students FROM Courses c;

--2. Identify the student(s) who made the highest payment. Use a subquery to find the maximum payment amount and then retrieve the student(s) associated with that amount.

SELECT s.first_name, s.student_id, p.amount FROM Students s JOIN Payments p ON s.student_id = p.student_id 
WHERE p.amount = (SELECT MAX(amount) FROM Payments);

--3. Retrieve a list of courses with the highest number of enrollments. Use subqueries to find the course(s) with the maximum enrollment count.

SELECT c.course_name, COUNT(e.student_id) AS enrollments FROM Courses c JOIN Enrollments e ON c.course_id = e.course_id GROUP BY c.course_name
HAVING COUNT(e.student_id) = (SELECT MAX(enrollment_count) FROM (SELECT COUNT(student_id) AS enrollment_count FROM Enrollments GROUP BY course_id) AS subquery);

--4. Calculate the total payments made to courses taught by each teacher. Use subqueries to sum payments for each teacher's courses.

SELECT t.first_name, SUM(p.amount) AS total_payments FROM Teacher t JOIN Courses c ON t.teacher_id = c.teacher_id JOIN Enrollments e ON c.course_id = e.course_id
JOIN Payments p ON e.student_id = p.student_id GROUP BY t.first_name;

--5. Identify students who are enrolled in all available courses. Use subqueries to compare a student's enrollments with the total number of courses.

SELECT s.first_name FROM Students s WHERE (SELECT COUNT(*) FROM Courses) = (SELECT COUNT(DISTINCT e.course_id) FROM Enrollments e WHERE e.student_id = s.student_id);

--6. Retrieve the names of teachers who have not been assigned to any courses. Use subqueries to find teachers with no course assignments.

SELECT t.first_name FROM Teacher t WHERE NOT EXISTS (SELECT 1 FROM Courses c WHERE c.teacher_id = t.teacher_id);

--7. Calculate the average age of all students. Use subqueries to calculate the age of each student based on their date of birth.

SELECT AVG(DATEDIFF(DATE(), s.dob) / 365) AS avg_age
FROM Students s;

--8. Identify courses with no enrollments. Use subqueries to find courses without enrollment records.

SELECT c.course_name FROM Courses c WHERE NOT EXISTS (SELECT 1 FROM Enrollments e WHERE e.course_id = c.course_id);

--9. Calculate the total payments made by each student for each course they are enrolled in. Use subqueries and aggregate functions to sum payments.

SELECT e.student_id, e.course_id, SUM(p.amount) AS total_payment
FROM Enrollments e JOIN Payments p ON e.student_id = p.student_id GROUP BY e.student_id, e.course_id;

--10. Identify students who have made more than one payment. Use subqueries and aggregate functions to count payments per student and filter for those with counts greater than one.

SELECT s.first_name,s. last_name FROM Students s
WHERE (SELECT COUNT(*) FROM Payments p WHERE p.student_id = s.student_id) > 1;


--11. Write an SQL query to calculate the total payments made by each student. Join the "Students" table with the "Payments" table and use GROUP BY to calculate the sum of payments for each student.

SELECT s.first_name, SUM(p.amount) AS total_payment
FROM Students s JOIN Payments p ON s.student_id = p.student_id GROUP BY s.first_name;

--12. Retrieve a list of course names along with the count of students enrolled in each course. Use JOIN operations between the "Courses" table and the "Enrollments" table and GROUP BY to count enrollments.

SELECT c.course_name, COUNT(e.student_id) AS enrollment_count FROM Courses c JOIN Enrollments e ON c.course_id = e.course_id GROUP BY c.course_name;

--13. Calculate the average payment amount made by students. Use JOIN operations between the "Students" table and the "Payments" table and GROUP BY to calculate the average.

SELECT AVG(p.amount) AS avg_payment FROM Payments p;

