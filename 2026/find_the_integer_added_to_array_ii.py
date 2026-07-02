"""
https://leetcode.com/problems/find-the-integer-added-to-array-ii/description/
"""


from collections import Counter
from heapq import nsmallest


class Solution:
    """
    Solution
    """

    def minimum_added_integer(self, nums1: list[int], nums2: list[int]) -> int:
        """
        minimum added integer
        """
        m2 = min(nums2)
        cnt = Counter(nums2)
        for x in reversed([m2 - v for v in nsmallest(3, nums1)]):
            if cnt <= Counter(y + x for y in nums1):
                return x

        return -1
