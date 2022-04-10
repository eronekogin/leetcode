"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            m = l + ((r - l) >> 1)
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m

        return l


print(Solution().peakIndexInMountainArray([0, 10, 5, 2]))
