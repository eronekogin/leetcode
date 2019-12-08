-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT E1.Name AS Employee
FROM Employee E1 left join Employee E2
ON E1.ManagerId = E2.Id
WHERE E1.Salary > E2.Salary