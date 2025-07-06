"""
https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/description/
"""


class Solution:
    """
    Solution
    """

    def min_increments(self, n: int, cost: list[int]) -> int:
        """
        min increments
        """
        total_cost = list(cost)
        increments = 0
        for i in range((n >> 1) - 1, -1, -1):
            left = (i << 1) + 1
            right = left + 1
            increments += abs(total_cost[left] - total_cost[right])
            total_cost[i] += max(total_cost[left], total_cost[right])

        return increments
