"""
https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_operations(self, nums: list[int]) -> int:
        """
        minimum operations
        """
        return len(set(nums) - {0})
