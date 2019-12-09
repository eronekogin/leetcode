-- https://leetcode.com/problems/customers-who-never-order/

SELECT C.Name As Customers
FROM Customers C LEFT JOIN Orders O
ON C.Id = O.CustomerId
WHERE O.Id IS NULL