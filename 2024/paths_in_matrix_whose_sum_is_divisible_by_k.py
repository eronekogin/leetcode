"""
https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_paths(self, grid: list[list[int]], k: int) -> int:
        """
        dp[i][j][m] stands for the number of paths with its sum % k == m,
        then our goal is to find dp[-1][-1][0].

        dp[i][j][m] can be calculated either from top or from left since
        we can only go down or go right to reach the right bottom cell.
        """
        m, n, mod = len(grid), len(grid[0]), 10 ** 9 + 7

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                for s in range(k):
                    mod_sum = (s + grid[i][j]) % k
                    if j > 0:
                        dp[i][j][mod_sum] += dp[i][j - 1][s]

                    if i > 0:
                        dp[i][j][mod_sum] += dp[i - 1][j][s]

                    dp[i][j][mod_sum] %= mod

        return dp[-1][-1][0]
