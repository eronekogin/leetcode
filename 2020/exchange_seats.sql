-- https://leetcode.com/problems/exchange-seats/


SELECT
    s1.id AS id,
    CASE
        WHEN s1.id & 1 = 0 THEN s3.student
        WHEN s2.student IS NULL THEN s1.student
        ELSE s2.student
    END AS student
FROM seat s1
LEFT OUTER JOIN seat s2
ON s1.id = s2.id - 1
LEFT OUTER JOIN seat s3
ON s1.id = s3.id + 1
;


-- Alternate solution, no need to join.
SELECT
    CASE
        WHEN id & 1 = 0 THEN id - 1
        WHEN id = counts THEN id
        ELSE id + 1 
    END AS id,
    student
FROM seat, 
    (
        SELECT COUNT(*) AS counts FROM seat
    ) AS seat_counts
ORDER BY id
;
