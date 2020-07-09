-- https: //data36.com/sql-interview-questions-tech-screening-data-analysts/

(1) -- Let’s say you have two SQL tables: authors and books. The authors dataset has 1M+ rows; here’s the first six rows:
-- Create an SQL query that shows the TOP 3 authors who sold the most books in total!

SELECT *
from authors a
    INNER JOIN books b
    ON a.book_name = b.book_name
GROUP BY a.author_name
ORDER BY b.sold_copies DESC
LIMIT 3

(2) -- Write an SQL query to find out how many users inserted more than 1000 but less than 2000 images in their presentations!

SELECT COUNT(*) FROM (
    SELECT user_id, COUNT(event_date_time) FROM event_log
    GROUP BY user_id
) AS image_per_user
WHERE image_per_user > 1000 AND image_per_user < 2000

(3) -- Print every department where the average salary per employee is lower than $500!

SELECT department_name, AVG(salary) FROM (
    SELECT * FROM employees
    INNER JOIN salaries
    ON employees.employee_id = salaries.employee_id
)
GROUP BY department_name
WHERE salary < 500




