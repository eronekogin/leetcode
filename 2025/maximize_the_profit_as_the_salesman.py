"""
https://leetcode.com/problems/maximize-the-profit-as-the-salesman/description/
"""


class Solution:
    """
    Solution
    """

    def maximize_the_profit(self, n: int, offers: list[list[int]]) -> int:
        """
        dp[i] stands for the maximum gold we can earn from the first ith
        houses.
        """
        dp = [0] * (n + 1)
        ends = [[] for _ in range(n)]
        for s, e, g in offers:
            ends[e].append([s, g])

        for e in range(1, n + 1):
            dp[e] = dp[e - 1]
            for s, g in ends[e - 1]:
                dp[e] = max(dp[e], dp[s] + g)

        return dp[-1]
