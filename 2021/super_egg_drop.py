"""
https://leetcode.com/problems/super-egg-drop/
"""


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
        Suppose dp[r][c] stands for the maximum floor we could solve when
        having r moves and c eggs. Then we have:
            dp[r][c] = 1 + dp[r - 1][c - 1] + dp[r - 1][c]

        Which means we drop 1 egg on a floor x, if it breaks, we could solve
        dp[r - 1][c - 1] lower floors than x; If it survies, we could solve
        dp[r - 1][c] higher floors than x.
        """
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for r in range(1, n + 1):
            for c in range(1, k + 1):
                dp[r][c] = dp[r - 1][c - 1] + dp[r - 1][c] + 1

            if dp[r][c] >= n:
                return r
