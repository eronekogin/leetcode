"""
https://leetcode.com/problems/collecting-chocolates/description/
"""


class Solution:
    """
    Solution
    """

    def min_cost(self, nums: list[int], x: int) -> int:
        """
        min cost
        """
        min_cost = sum(nums)
        for r in range(1, len(nums)):
            nums = [min(nums[i], nums[i - 1]) for i in range(len(nums))]
            min_cost = min(min_cost, r * x + sum(nums))

        return min_cost
