"""
https://leetcode.com/problems/longest-continuous-increasing-subsequence/
"""


from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxLen = start = 0
        n = len(nums)
        for end in range(1, n):
            if nums[end] <= nums[end - 1]:
                maxLen = max(maxLen, end - start)
                start = end

        return max(maxLen, n - start)
