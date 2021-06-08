"""
https://leetcode.com/problems/smallest-range-i/
"""


class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        currMin, currMax = min(nums), max(nums)

        # (currMax - k) - (currMin + k)
        return max(0, currMax - currMin - (k << 1))
