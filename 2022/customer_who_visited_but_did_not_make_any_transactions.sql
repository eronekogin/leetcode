-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

select
    customer_id, count(*) as count_no_trans
from
    visits
where
    visit_id not in (
        select
            distinct visit_id
        from
            transactions
    )
group by
    customer_id

