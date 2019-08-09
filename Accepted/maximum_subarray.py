"""
https://leetcode.com/problems/maximum-subarray/
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Take dp[i] as the max sub array which contains nums[i] at its end.
        Then dp[i + 1] = dp[i] > 0 ? dp[i] : 0.
        """
        currMax = currSum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum + num)
            currMax = max(currMax, currSum)

        return currMax


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
