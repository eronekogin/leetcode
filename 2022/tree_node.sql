-- https://leetcode.com/problems/tree-node/


select
    t.id as id,
    case
        when t.p_id is null then 'Root'
        when p.has_child is not null then 'Inner'
        else 'Leaf'
    end as type
from tree t
left join
(
    select p_id as id, true as has_child
    from tree
    group by p_id
    having count(*) > 0
) as p
on t.id = p.id
order by 1