"""
https://leetcode.com/problems/maximum-size-of-a-set-after-removals/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_set_size(self, nums1: list[int], nums2: list[int]) -> int:
        """
        maximum set size
        """
        half = len(nums1) >> 1
        s1 = set(nums1)
        s2 = set(nums2)
        overlap = len(s1 & s2)

        v1 = min(len(s1) - overlap, half)
        v2 = min(len(s2) - overlap, half)

        return min(v1 + v2 + overlap, len(nums1))
