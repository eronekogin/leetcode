"""
https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
"""


class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        sortedNums = sorted(nums, reverse=True)
        total = sum(nums)
        currSum = 0
        for i, num in enumerate(sortedNums):
            currSum += num
            if (currSum << 1) > total:
                return sortedNums[:(i + 1)]
