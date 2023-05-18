"""
https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
"""


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        if len(arr) == 1:
            return 1

        currMax = 0
        for num in sorted(arr):
            currMax = min(currMax + 1, num)

        return currMax
