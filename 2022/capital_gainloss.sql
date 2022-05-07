-- https://leetcode.com/problems/capital-gainloss/

select stock_name, sum(
    case operation
        when 'Buy' then -price
        else price
    end
) as capital_gain_loss
from stocks
group by stock_name
