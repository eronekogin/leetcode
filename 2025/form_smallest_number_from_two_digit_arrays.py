"""
https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/description/
"""


class Solution:
    """
    Solution
    """

    def min_number(self, nums1: list[int], nums2: list[int]) -> int:
        """
        min number
        """
        candidates = set(nums1) & set(nums2)
        if candidates:
            return min(candidates)

        m1, m2 = min(nums1), min(nums2)
        if m1 >= m2:
            return m2 * 10 + m1

        return m1 * 10 + m2
