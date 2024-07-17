"""
https://leetcode.com/problems/selling-pieces-of-wood/description/
"""


class Solution:
    """
    Solution
    """

    def selling_wood(self, m: int, n: int, prices: list[list[int]]) -> int:
        """
        selling wood
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = p

        for h in range(1, m + 1):
            for w in range(1, n + 1):
                for r in range(1, (h >> 1) + 1):
                    dp[h][w] = max(
                        dp[h][w],
                        dp[r][w] + dp[h - r][w]
                    )

                for c in range(1, (w >> 1) + 1):
                    dp[h][w] = max(
                        dp[h][w],
                        dp[h][c] + dp[h][w - c]
                    )

        return dp[-1][-1]


print(Solution().selling_wood(3, 5, [[1, 4, 2], [2, 2, 7], [2, 1, 3]]))
