"""
https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 1

        dp = [0, 1, 1] + [0] * (n - 2)
        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        return dp[-1]


print(Solution().tribonacci(25))
