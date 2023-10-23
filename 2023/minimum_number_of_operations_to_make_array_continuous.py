"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
"""

from bisect import bisect_right


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int]) -> int:
        """
        min_operations
        """
        n = len(nums)
        sorted_unique_nums = sorted(set(nums))

        min_operations = n
        for i, start in enumerate(sorted_unique_nums):
            end = start + n - 1
            j = bisect_right(sorted_unique_nums, end)
            unique_items = j - i
            min_operations = min(min_operations, n - unique_items)

        return min_operations
