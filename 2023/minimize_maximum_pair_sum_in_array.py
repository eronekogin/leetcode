"""
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
"""


class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        N = len(nums)
        sortedNums = sorted(nums)
        return max(
            sortedNums[i] + sortedNums[N - 1 - i]
            for i in range(N >> 1)
        )