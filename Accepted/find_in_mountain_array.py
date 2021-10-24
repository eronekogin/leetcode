"""
https://leetcode.com/problems/find-in-mountain-array/
"""


from test_helper import MountainArray


class Solution:
    def findInMountainArray(
        self, target: int, mountain_arr: MountainArray
    ) -> int:
        """
        1. Use binary search to find the peak in the mountain array.
        2. Then use binary search on each half to check if target exists.
        """
        N = mountain_arr.length()

        # Find peak.
        l, r = 0, N - 1
        while l < r:
            m = l + ((r - l) >> 1)
            if mountain_arr.get(m) > mountain_arr.get(m + 1):  # Down.
                r = m
            else:
                l = m + 1

        peak = l

        # Search left increasing part.
        l, r = 0, peak
        while l <= r:
            m = l + ((r - l) >> 1)
            if mountain_arr.get(m) > target:
                r = m - 1
            elif mountain_arr.get(m) < target:
                l = m + 1
            else:
                return m

        # Search right decreasing part.
        l, r = peak, N - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if mountain_arr.get(m) > target:
                l = m + 1
            elif mountain_arr.get(m) < target:
                r = m - 1
            else:
                return m

        return -1  # Not found.


print(Solution().findInMountainArray(2, MountainArray([1, 2, 3, 4, 5, 3, 1])))
