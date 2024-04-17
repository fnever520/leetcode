SELECT
    c.Name, MAX(o.PRICE)
FROM
    CUSTOMERS c
JOIN ORDERS o
ON
    c.ORDER_ID = o.ID
WHERE
    o.ORDER_DATE >= (
    SELECT MIN(ORDER_DATE) FROM ORDERS)
    AND
    o.ORDER_DATE <= DATE_ADD((SELECT MIN(ORDER_DATE) from ORDERS), INTERVAL 10 YEAR)
GROUP BY c.NAME
ORDER BY o.PRICE DESC
limit 1;

"""
from the data table, determine the location having the most companies. List the name of the employess who work in that location and the names of their companies. The output should consists of two columns: PEOPLE.name COMPANIES.name. the row can be in any order
"""

SELECT
    p.name, c.name
FROM
    people p
JOIN
    COMPANIES c
ON
    p.company_id = c.id
JOIN
    LOCATIONS l
ON
    c.LOCATION_ID = l.id
WHERE
    l.name =   
    (
        SELECT location2.name
        FROM LOCATIONS location2
        JOIN COMPANIES c2
        ON c2.LOCATION_ID = location2.ID
        GROUP BY location2.NAME
        ORDER BY COUNT(*) DESC
        limit 1
    )
ORDER BY p.name;
