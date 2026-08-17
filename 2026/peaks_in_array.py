"""
https://leetcode.com/problems/peaks-in-array/description/
"""

from sortedcontainers import SortedList


class Solution:
    """
    Solution
    """

    def count_of_peaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        count of peaks
        """
        peaks = SortedList(
            i
            for i in range(1, len(nums) - 1)
            if nums[i - 1] < nums[i] > nums[i + 1]
        )
        rslt: list[int] = []

        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                start = peaks.bisect_right(l)
                end = peaks.bisect_left(r) - 1
                rslt.append(max(end - start + 1, 0))
            else:
                i, v = q[1], q[2]
                nums[i] = v

                for j in (i - 1, i, i + 1):
                    peaks.discard(j)
                    if 0 < j < len(nums) - 1 and nums[j - 1] < nums[j] > nums[j + 1]:
                        peaks.add(j)

        return rslt
