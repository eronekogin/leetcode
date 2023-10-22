"""
https://leetcode.com/problems/maximum-earnings-from-taxi/
"""


class Solution:
    """
    Solution
    """

    def max_taxi_earnings(self, n: int, rides: list[list[int]]) -> int:
        """
        dp[i] stands for the maximum money we can earn starting at point i, the we have:
            * We don't pick up passenger at point i, so dp[i] = dp[i + 1]
            * We pick up passenger at point i, and we will have dp[i] = dp[end] + end - start + tip
        Then we get the maximum result from the above cases.
        """
        dp = [0] * (n + 1)
        rides.sort()
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]
            while rides and i == rides[-1][0]:
                start, end, tip = rides.pop()
                dp[i] = max(dp[i], dp[end] + end - start + tip)

        return dp[0]
