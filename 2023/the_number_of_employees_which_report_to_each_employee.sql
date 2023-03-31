-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/


select
    s.reports_to as employee_id,
    t.name as name,
    count(*) as reports_count,
    round(avg(s.age)) as average_age
from employees s join employees t
on s.reports_to = t.employee_id
group by s.reports_to
order by 1

