"""
https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_cost(self, cost: list[int]) -> int:
        """
        minimum_cost
        """
        sorted_cost = sorted(cost, reverse=True)
        min_cost = 0
        for i in range(1, len(cost) + 1):
            if i % 3 == 0:
                continue

            min_cost += sorted_cost[i - 1]

        return min_cost
