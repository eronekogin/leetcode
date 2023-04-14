"""
https://leetcode.com/problems/maximum-ascending-subarray-sum/
"""


class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        i, n = 0, len(nums)
        maxSum = 0
        while i < n:
            currMax = nums[i]
            while i + 1 < n and nums[i + 1] > nums[i]:
                i += 1
                currMax += nums[i]

            maxSum = max(maxSum, currMax)
            i += 1

        return maxSum
