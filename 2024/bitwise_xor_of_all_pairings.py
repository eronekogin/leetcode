"""
https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/
"""


from functools import reduce
from operator import xor


class Solution:
    """
    Solution
    """

    def xor_all_nums(self, nums1: list[int], nums2: list[int]) -> int:
        """
        xor all nums
        """
        l1, l2 = len(nums1), len(nums2)

        rslt = 0

        if l1 & 1:
            rslt ^= reduce(xor, nums2)

        if l2 & 1:
            rslt ^= reduce(xor, nums1)

        return rslt
