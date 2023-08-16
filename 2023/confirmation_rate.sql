-- https://leetcode.com/problems/confirmation-rate/


select
    signups.user_id as user_id,
    round(ifnull(C.confirmedCounter, 0) / ifnull(B.totalCounter, 1), 2) as confirmation_rate
from
    signups
left outer join
    (
        select user_id, count(*) as totalCounter
        from confirmations
        group by user_id
    ) as B
on signups.user_id = B.user_id
left outer join
    (
        select user_id, count(*) as confirmedCounter
        from confirmations
        where action = 'confirmed'
        group by user_id
    ) as C 
on B.user_id = C.user_id