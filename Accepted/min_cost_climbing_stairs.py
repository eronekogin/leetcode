"""
https://leetcode.com/problems/min-cost-climbing-stairs/
"""


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N + 1)
        for i in range(2, N + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[-1]
