"""
https://leetcode.com/problems/sorting-three-groups/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_operations(self, nums: list[int]) -> int:
        """
        dp[k] stands for the number of operations we need
        to transform nums from 1 to k non-decreasingly.
        Each time we found a number, we save one delete
        operation
        """
        n = len(nums)
        dp = [n] * 4

        for x in nums:
            dp[x] -= 1
            dp[2] = min(dp[2], dp[1])
            dp[3] = min(dp[3], dp[2])

        return dp[3]
