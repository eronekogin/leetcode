-- https://leetcode.com/problems/patients-with-a-condition/


select *
from patients
where conditions like '% DIAB1%'
or conditions like 'DIAB1%'
