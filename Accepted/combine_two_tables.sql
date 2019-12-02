-- https://leetcode.com/problems/combine-two-tables/


-- Write your MySQL query statement below
select p.FirstName, p.LastName, a.City, a.State
from Person as p left outer join Address as a
on p.PersonId = a.PersonId
;
