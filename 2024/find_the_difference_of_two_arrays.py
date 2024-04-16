"""
https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
"""


class Solution:
    """
    Solution
    """

    def find_difference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """
        find difference
        """
        s1, s2 = set(nums1), set(nums2)
        return [
            list(s1 - s2),
            list(s2 - s1)
        ]
