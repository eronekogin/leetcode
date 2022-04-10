"""
https://leetcode.com/problems/sum-of-subsequence-widths/
"""


class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        """
        1. The width of subsequences is defined by the difference between the
            maximum and minimum number in this subsequence, so the order does
            not matter.
        2. Then we could sort the nums and for the ith number in the sorted
            list:
            2.1 There are 2^i subsequences having nums[i] as its maximum.
            2.2 There are 2^(n - 1 - i) subsequences having nums[i] as its
                mininum.
        """
        N = len(nums) - 1
        rslt = sum(
            ((1 << i) - (1 << (N - i))) * v
            for i, v in enumerate(sorted(nums)))
        return rslt % (10 ** 9 + 7)
