--- https://leetcode.com/problems/market-analysis-i/


select u.user_id as buyer_id, u.join_date as join_date, ifnull(t.orders_in_2019, 0) as orders_in_2019
from
users u left join
(
    select buyer_id, count(*) as orders_in_2019
    from orders
    where year(order_date) = '2019'
    group by buyer_id
) as t
on t.buyer_id = u.user_id