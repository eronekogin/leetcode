-- https://leetcode.com/problems/not-boring-movies/


SELECT *
FROM cinema
WHERE id & 1 = 1
AND description <> 'boring'
ORDER BY rating DESC
;