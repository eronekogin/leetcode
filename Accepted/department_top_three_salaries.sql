-- https://leetcode.com/problems/department-top-three-salaries/

SELECT
    D.Name AS Department,
    E1.Name as Employee,
    E1.Salary
FROM
    Department D,
    Employee E1,
    Employee E2
WHERE D.Id = E1.DepartmentId
AND E1.DepartmentId = E2.DepartmentId
AND E1.Salary <= E2.Salary
GROUP BY D.Id, E1.Name
HAVING COUNT(DISTINCT E2.Salary) <= 3
ORDER BY 1, 3 DESC