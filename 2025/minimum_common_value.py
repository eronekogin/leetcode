"""
https://leetcode.com/problems/minimum-common-value/description/
"""


class Solution:
    """
    Solution
    """

    def get_common(self, nums1: list[int], nums2: list[int]) -> int:
        """
        get common
        """
        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]:
            return -1

        i1 = i2 = 0
        n1, n2 = len(nums1), len(nums2)
        while i1 < n1 and i2 < n2:
            while i1 < n1 and nums1[i1] < nums2[i2]:
                i1 += 1

            if i1 == n1:
                break

            if nums1[i1] == nums2[i2]:
                return nums1[i1]

            while i2 < n2 and nums2[i2] < nums1[i1]:
                i2 += 1

        return -1


print(Solution().get_common([1, 3], [2, 4]))
