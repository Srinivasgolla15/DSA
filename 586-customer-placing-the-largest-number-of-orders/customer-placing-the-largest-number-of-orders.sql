# Write your MySQL query statement below
-- SELECT CUSTOMER_NUMBER
-- FROM (
--     SELECT CUSTOMER_NUMBER, COUNT(CUSTOMER_NUMBER) AS counts
--     FROM ORDERS
--     GROUP BY CUSTOMER_NUMBER
-- ) AS T
-- WHERE counts = (
--     SELECT MAX(counts)
--     FROM (
--         SELECT CUSTOMER_NUMBER, COUNT(CUSTOMER_NUMBER) AS counts
--         FROM ORDERS
--         GROUP BY CUSTOMER_NUMBER
--     ) AS X
-- )
-- LIMIT 1;


SELECT 
    customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC 
LIMIT 1;  