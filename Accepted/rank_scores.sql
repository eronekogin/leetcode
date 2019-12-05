-- https://leetcode.com/problems/rank-scores/

SELECT
    Score,
    (
        SELECT COUNT(*)
        FROM (
            SELECT DISTINCT Score AS s
            FROM Scores
        ) AS Temp
        WHERE Temp.s >= Score 
    ) AS Rank
FROM Scores
ORDER BY Score DESC