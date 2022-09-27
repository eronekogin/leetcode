-- https://leetcode.com/problems/bank-account-summary-ii/

select
    u.name as name, 
    sum(t.amount) as balance
from
    transactions t left outer join users u
    on t.account = u.account
group by
    t.account
having
    sum(t.amount) > 10000

    

