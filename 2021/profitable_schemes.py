"""
https://leetcode.com/problems/profitable-schemes/
"""


class Solution:
    def profitableSchemes(
            self, n: int,
            minProfit: int,
            group: list[int],
            profit: list[int]) -> int:
        """
        Suppose dp[i][j] stands for the total schemes with profit as i and
        members as j. Then we have:

        dp[i + p][j + g] += dp[i][j] if i + p < minProfit
        dp[minProfit][j + g] += dp[i][j] if i + p >= minProfit
        """
        dp = [[0] * (n + 1) for _ in range(minProfit + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(minProfit, -1, -1):
                for j in range(n - g, -1, -1):
                    dp[min(i + p, minProfit)][j + g] += dp[i][j]

        return sum(dp[minProfit]) % (10 ** 9 + 7)
