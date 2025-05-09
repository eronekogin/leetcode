"""
https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/description/
"""


from bisect import bisect_left
from itertools import accumulate


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int], queries: list[int]) -> list[int]:
        """
        For x in nums < q, need operations q * i - sum(x)
        For x in nums >= q, need operations sum(x) - q * i
        """
        nums.sort()
        n = len(nums)
        pre_sums = list(accumulate(nums, initial=0))
        rslt: list[int] = [0] * len(queries)
        for j, x in enumerate(queries):
            i = bisect_left(nums, x)
            rslt[j] = x * (2 * i - n) + pre_sums[n] - 2 * pre_sums[i]

        return rslt
