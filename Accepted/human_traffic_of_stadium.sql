-- https://leetcode.com/problems/human-traffic-of-stadium/

SELECT DISTINCT T1.*
FROM stadium T1
JOIN stadium T2
JOIN stadium T3
ON (
    (T1.id = T2.id - 1 AND T1.id = T3.id - 2) -- t1, t2, t3
    OR (T1.id = T2.id + 1 AND T1.id = T3.id - 1)  -- t2, t1, t3
    OR (T1.id = T2.id + 1 AND T1.id = T3.id + 2)  -- t3, t2, t1
)
WHERE T1.people >= 100 AND T2.people >= 100 AND T3.people >= 100
ORDER BY T1.id
;