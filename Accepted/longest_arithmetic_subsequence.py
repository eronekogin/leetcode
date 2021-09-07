"""
https://leetcode.com/problems/longest-arithmetic-subsequence/
"""


class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        """
        Suppose dp[i][diff] stands for the length of arithmatic sequence 
        ending at index i with difference as diff, then we have:
        dp[j][nums[j] - nums[i]] = dp[i][nums[j] - nums[i]] + 1
        """
        dp, N = {}, len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                diff = nums[j] - nums[i]
                dp[(j, diff)] = dp.get((i, diff), 1) + 1

        return max(dp.values())
