"""
https://leetcode.com/problems/merge-sorted-array/
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, i3 = m - 1, n - 1, m + n - 1
        while i1 > -1 and i2 > -1:
            if nums1[i1] < nums2[i2]:
                nums1[i3] = nums2[i2]
                i2 -= 1
            else:
                nums1[i3] = nums1[i1]
                i1 -= 1

            i3 -= 1

        while i2 > -1:
            # If some of the numbers in nums2 are less than the minimum
            # number in nums1.
            nums1[i3] = nums2[i2]
            i2 -= 1
            i3 -= 1


nums1 = [2, 0]
nums2 = [1]
m, n = 1, 1
print(Solution().merge(nums1, m, nums2, n))
print(nums1)
