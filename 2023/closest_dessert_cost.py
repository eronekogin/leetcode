"""
https://leetcode.com/problems/closest-dessert-cost/
"""


class Solution:
    def closestCost(
        self,
        baseCosts: list[int],
        toppingCosts: list[int],
        target: int
    ):
        toppingCostSums = {0}
        for cost in toppingCosts:
            nextToppingCostSums = set(toppingCostSums)
            for costSum in toppingCostSums:
                nextToppingCostSums.add(costSum + cost)
                nextToppingCostSums.add(costSum + 2 * cost)

            toppingCostSums = nextToppingCostSums

        rslt = minDiff = float('inf')
        for baseCost in baseCosts:
            for topCost in toppingCostSums:
                totalCost = baseCost + topCost
                currDiff = abs(totalCost - target)
                if currDiff < minDiff:
                    rslt, minDiff = totalCost, currDiff
                elif currDiff == minDiff and totalCost < rslt:
                    rslt = totalCost

        return rslt
