-- 1. Using CASE WHEN

SELECT
    P.product_id,
    ROUND(
        CASE
            WHEN SUM(U.units) IS NULL OR SUM(U.units) = 0 THEN 0
            ELSE SUM(P.price * U.units) / SUM(U.units)
        END,
        2
    ) AS average_price
FROM Prices P
LEFT JOIN UnitsSold U
    ON P.product_id = U.product_id
    AND U.purchase_date >= P.start_date
    AND U.purchase_date <= P.end_date
GROUP BY P.product_id;


-- 2. Using IFNULL()

-- SELECT
--     P.product_id,
--     IFNULL(
--         ROUND(
--             SUM(P.price * U.units) / SUM(U.units),
--             2
--         ),
--         0
--     ) AS average_price
-- FROM Prices P
-- LEFT JOIN UnitsSold U
--     ON P.product_id = U.product_id
--     AND U.purchase_date >= P.start_date
--     AND U.purchase_date <= P.end_date
-- GROUP BY P.product_id;


-- -- 3. Using COALESCE()

-- SELECT
--     P.product_id,
--     ROUND(
--         COALESCE(
--             SUM(P.price * U.units) / SUM(U.units),
--             0
--         ),
--         2
--     ) AS average_price
-- FROM Prices P
-- LEFT JOIN UnitsSold U
--     ON P.product_id = U.product_id
--     AND U.purchase_date >= P.start_date
--     AND U.purchase_date <= P.end_date
-- GROUP BY P.product_id;