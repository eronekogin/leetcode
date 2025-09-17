"""
https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/description/
"""


class Solution:
    """
    Solution
    """

    def max_non_decreasing_length(self, nums1: list[int], nums2: list[int]) -> int:
        """
        dp1[i] means the maximum steps ending with nums1[i]
        dp2[i] means the maximum steps ending with nums2[i]
        """
        rslt = dp1 = dp2 = 1

        for i in range(1, len(nums1)):
            t11 = dp1 + 1 if nums1[i - 1] <= nums1[i] else 1
            t12 = dp1 + 1 if nums1[i - 1] <= nums2[i] else 1
            t21 = dp2 + 1 if nums2[i - 1] <= nums1[i] else 1
            t22 = dp2 + 1 if nums2[i - 1] <= nums2[i] else 1

            dp1 = max(t11, t21)
            dp2 = max(t12, t22)
            rslt = max(rslt, dp1, dp2)

        return rslt
