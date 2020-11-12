-- IF OBJECT_ID('student') IS NOT NULL
-- BEGIN 
-- DROP TABLE student
-- END 

-- CREATE TABLE student(
--     student_id INT,
--     name VARCHAR(200) NOT NULL,
--     major VARCHAR(200) DEFAULT 'undecided',
--     PRIMARY KEY(student_id)
-- );

-- INSERT INTO student VALUES(1, 'Jack', 'Biology');
-- INSERT INTO student VALUES(2, 'Kate', 'Sociology');
-- INSERT INTO student VALUES(4, 'Fabian', 'computer');
-- INSERT INTO student(student_id, name) VALUES(3, 'Claire');


SELECT * FROM student;
-- UPDATE student
-- SET major = 'CS'
-- WHERE major = 'computer'

-- SELECT *
-- FROM student;
-- DELETE FROM student
-- WHERE major = 'Bio';

SELECT student.name, student.major
FROM student
ORDER BY major DESC