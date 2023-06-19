"""
https://leetcode.com/problems/calculate-special-bonus/
"""


select
    employee_id,
    case
        when mod(employee_id, 2) = 1 && name not like 'M%' then salary
        else 0
    end as bonus
from employees
order by employee_id