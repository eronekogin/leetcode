"""
https://leetcode.com/problems/two-out-of-three/
"""


class Solution:
    """
    Solution
    """

    def two_out_of_three(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        """
        two_out_of_three
        """
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        return list((s1 & s2) | (s2 & s3) | (s1 & s3))
