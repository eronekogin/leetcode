"""
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
"""


class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        minPrefixSum = float('inf')
        currPrefixSum = 0
        for num in nums:
            currPrefixSum += num
            minPrefixSum = min(minPrefixSum, currPrefixSum)

        if minPrefixSum >= 0:
            return 1  # start value must be positive.

        return -minPrefixSum + 1
