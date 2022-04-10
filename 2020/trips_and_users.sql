-- https://leetcode.com/problems/trips-and-users/


SELECT
    Request_at AS Day,
    ROUND(SUM(Status != 'completed') / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips T
JOIN Users C ON
    T.Client_Id = C.Users_Id
JOIN Users D ON
    T.Driver_Id = D. Users_Id
WHERE
    C.Banned = 'No'
AND D.Banned = 'No'
AND Request_at BETWEEN DATE('2013-10-01') AND DATE('2013-10-03')
GROUP BY Request_at
;

