-- https://leetcode.com/problems/department-highest-salary/

SELECT
    D.Name AS Department,
    E.Name AS Employee,
    E.Salary As Salary
FROM 
    (
        SELECT DepartmentId, max(Salary) AS Salary
        FROM Employee
        GROUP BY DepartmentId
    ) AS R,
    Employee E,
    Department D
WHERE R.DepartmentId = E.DepartmentId
AND R.Salary = E.Salary
AND R.DepartmentId = D.Id