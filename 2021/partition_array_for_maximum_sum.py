"""
https://leetcode.com/problems/partition-array-for-maximum-sum/
"""


class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        """
        Suppose dp[i] stands for the maximum sum we could get from arr[0]
        to arr[i], then we have:
            dp[i] = max(dp[i-j] + max(arr[i-j:i+1]) * j for j in (1, k))
        """
        N = len(arr)
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            currMax = 0
            for j in range(1, min(k, i) + 1):
                currMax = max(currMax, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + currMax * j)

        return dp[N]
