-- https://leetcode.com/problems/employees-whose-manager-left-the-company/


select
    e1.employee_id as employee_id
from
    employees e1
    left join employees e2
    on e1.manager_id = e2.employee_id
where
        e1.manager_id is not null
    and e2.employee_id is null
    and e1.salary < 30000
order by 1