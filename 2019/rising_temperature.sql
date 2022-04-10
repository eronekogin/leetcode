-- https://leetcode.com/problems/rising-temperature/


SELECT W2.Id
FROM Weather W1, Weather W2
WHERE DATEDIFF(W2.RecordDate, W1.RecordDate) = 1
AND W2.Temperature > W1.Temperature