-- https://leetcode.com/problems/employees-with-missing-information/

select * from
(
    select n.employee_id as employee_id
    from employees n left join salaries s
    on n.employee_id = s.employee_id
    where s.salary is null

    union

    select s.employee_id as employee_id
    from salaries s left join employees n
    on s.employee_id = n.employee_id
    where n.name is null
) as T
order by 1

