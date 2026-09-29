"""
https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/description/
"""


from itertools import pairwise


class Solution:
    """
    Solution
    """

    def minimum_operations(self, nums: list[int], target: list[int]) -> int:
        """
        minimum operations
        """
        diffs = [y - x for x, y in zip(nums, target)]

        # Still only count for positive difference between two adjacent diff
        # The positive action cannot cross boundary
        return sum(
            max(y - x, 0)
            for x, y in pairwise([0] + diffs + [0])
        )
