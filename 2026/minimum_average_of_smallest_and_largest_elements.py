"""
https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_average(self, nums: list[int]) -> float:
        """
        minimum average
        """
        nums.sort()
        n = len(nums)
        return min(
            (nums[i] + nums[n - 1 - i]) / 2
            for i in range(n >> 1)
        )
