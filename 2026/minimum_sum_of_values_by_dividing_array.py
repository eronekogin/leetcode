"""
https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/description/
"""


from functools import cache
from math import inf


class Solution:
    """
    Solution
    """

    def minimum_value_sum(self, nums: list[int], and_values: list[int]) -> int:
        """
        minimum value sum
        """
        @cache
        def check(i: int, j: int, mask: int):
            if i == m and j == n:
                return 0

            if i == m or j == n:
                return inf

            mask &= nums[i]

            if mask < and_values[j]:
                return inf

            if mask == and_values[j]:
                return min(
                    check(i + 1, j, mask),
                    nums[i] + check(i + 1, j + 1, -1)
                )

            return check(i + 1, j, mask)

        m, n = len(nums), len(and_values)
        rslt = check(0, 0, -1)

        if rslt < inf:
            return int(rslt)

        return -1
