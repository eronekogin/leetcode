"""
https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/
"""


class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        i = j = 0
        maxDistance = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                maxDistance = max(maxDistance, j - i)
                j += 1

        return maxDistance


print(Solution().maxDistance(
    nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]))
