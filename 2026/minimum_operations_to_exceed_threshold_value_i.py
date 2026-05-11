"""
https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/description/
"""


from bisect import bisect_left


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int], k: int) -> int:
        """
        min operations
        """
        return bisect_left(sorted(nums), k)
