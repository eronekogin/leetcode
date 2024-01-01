"""
https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
"""


class Solution:
    """
    Solution
    """

    def minimum_deletions(self, nums: list[int]) -> int:
        """
        minimum_deletions
        """
        min_index, max_index = nums.index(min(nums)), nums.index(max(nums))
        n = len(nums)
        return min(
            1 + max(min_index, max_index),  # From left
            max(n - max_index, n - min_index),  # From right
            min_index + 1 + n - max_index,  # left + right
            max_index + 1 + n - min_index  # left + right
        )
