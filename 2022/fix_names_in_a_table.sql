-- https://leetcode.com/problems/fix-names-in-a-table/

select
    user_id,
    concat(
        upper(substr(name, 1, 1)),  -- substr posistion is 1 indexed.
        lower(substr(name, 2))
    ) as name
from
    users
order by 1
