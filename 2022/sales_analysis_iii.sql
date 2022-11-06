-- https://leetcode.com/problems/sales-analysis-iii/

select c.product_id as product_id, p.product_name as product_name
from (
    select distinct product_id
    from sales
    where sale_date between '2019-01-01' and '2019-03-31'
) as c left join product p on c.product_id = p.product_id
where c.product_id not in (
    select distinct product_id
    from sales
    where sale_date not between '2019-01-01' and '2019-03-31'
)
