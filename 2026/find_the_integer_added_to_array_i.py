"""
https://leetcode.com/problems/find-the-integer-added-to-array-i/description/
"""


class Solution:
    """
    Solution
    """

    def added_integer(self, nums1: list[int], nums2: list[int]) -> int:
        """
        added integer
        """
        return min(nums2) - min(nums1)
