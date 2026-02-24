"""
https://leetcode.com/problems/find-common-elements-between-two-arrays/description/
"""


class Solution:
    """
    Solution
    """

    def find_intersection_values(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        find intersection values
        """
        s1, s2 = set(nums1), set(nums2)
        return [
            sum(x in s2 for x in nums1),
            sum(x in s1 for x in nums2)
        ]
