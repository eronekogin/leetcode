"""
https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/
"""


class Solution:
    """
    Solution
    """

    def min_cost(self, nums: list[int], cost: list[int]) -> int:
        """
        min cost
        """
        median_cost = sum(cost) >> 1
        curr_cost = 0
        t = 0
        for x, c in sorted(zip(nums, cost)):
            curr_cost += c
            if curr_cost > median_cost:
                t = x
                break

        return sum(abs(x - t) * c for x, c in zip(nums, cost))
