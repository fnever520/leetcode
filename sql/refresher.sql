-- publisher_info               consumption_info
-- - video_id                   - video_id
-- - video_duration             - user_id
--                              - user_timespend

-- how many minutes worth of video does an average publisher have?
-- how many publishers have at least one user who watched their videos

SELECT SUM(video_duration)/COUNT(distinct video_id) FROM publisher_info


SELECT COUNT(distinct video_id) FROM publisher_info a
INNER JOIN consumption_info b
ON a.video_id = b.video_id



-- Q1 - return employee record with max salary
SELECT * FROM employee
WHERE salary = (SELECT MAX(salary) from employee)

-- Q2 - select the highest salary
SELECT Max(salary) FROM employee

-- Q3 - select 2nd highest salary in employee table
SELECT Max(salary) FROM employee
where salary NOT IN (
    SELECT Max(salary) FROM employee
)

-- Q4 - select range of employee based on id
SELECT * from employee 
where employee.id between 2002 and 2003

-- Q4 - return employee name, highest salary, and department
SELECT e.first_name, e.last_name, e.salary, d.department FROM employee e, 
INNER JOIN department d 
ON e.department_id = d.department_id
WHERE salary = (SELECT Max(salary) FROM employee)

-- Q5: return highest salary, employee name, department name from each department

SELECT e.first_name, e.last_name, e.salary, d.department FROM employee e
INNER JOIN department d
ON e.employee_id = d.employee_id
WHERE salary = (SELECT Max(salary) from employee GROUP BY department)