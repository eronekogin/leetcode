"""
https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_ways(self, n: int, x: int) -> int:
        """
        number of ways
        """
        m = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            v = i ** x
            if v > n:
                break

            for j in range(n, v - 1, -1):
                dp[j] = (dp[j] + dp[j - v]) % m

        return dp[n]
