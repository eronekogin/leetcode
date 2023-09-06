"""
https://leetcode.com/problems/count-number-of-special-subsequences/
"""


class Solution:
    def countSpecialSubsequences(self, nums: list[int]) -> int:
        """
        dp[0] stands for the number of subsequence with special number 0
        dp[1] stands for the number of subsequence with special number 01
        dp[2] stands for the number of subsequence with special number 012

        so we have:
            1. when current number is 0, it generates dp[0] + 1 new sequences.
            2. when current number is 1, it generates dp[0] + dp[1] new sequences.
            3. when current number is 2, it generates dp[1] + dp[2] new sequences.
        """
        dp = [1, 0, 0, 0]
        MOD = 10 ** 9 + 7
        for num in nums:
            dp[num + 1] = (dp[num] + dp[num + 1] * 2) % MOD
        
        return dp[-1] % MOD
        