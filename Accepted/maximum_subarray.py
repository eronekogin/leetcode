"""
https://leetcode.com/problems/maximum-subarray/
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Take dp[i] as the max sub array which contains nums[i] at its end.
        Then dp[i + 1] = nums[i + 1] + max(0, dp[i])
        """
        currMax, maxSum = 0, float('-inf')
        for num in nums:
            currMax = num + max(currMax, 0)
            maxSum = max(maxSum, currMax)

        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
