-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

select customer_number
from (
    select customer_number, count(*) as total_orders
    from orders
    group by customer_number
    order by total_orders desc
) as x
limit 1