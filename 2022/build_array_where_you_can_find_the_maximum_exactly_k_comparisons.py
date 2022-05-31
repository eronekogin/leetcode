"""
https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
"""


class Solution:
    def numOfArrays(self, N: int, M: int, K: int) -> int:
        """
        Suppose dp[n][k][m] stands for the maximum number of ways to construct
        the array when the length of the array is n, the maximum cost is k and
        the maximum number in the array is m, then we have:

            1. Don't jump on the current step, which means the maximum number
                the current array is less or equal to m, so we have:
                    dp[n][k][m] += sum(dp[n - 1][k][m] * m)
            2. Jump on the current step, which means the previous maximum
                number in the array must be less than m, so we have:
                    dp[n][k][m] += sum(
                        dp[n - 1][k - 1][mm]
                        for mm in range(1, m)
                    ) 
        """
        dp = [
            [
                [0] * (M + 1)
                for _ in range(K + 1)
            ]
            for _ in range(N + 1)
        ]

        # Base case: there is only 1 way for a single item array with jump 1.
        for m in range(1, M + 1):
            dp[1][1][m] = 1

        # Calculate dp.
        for n in range(1, N + 1):
            for k in range(1, K + 1):
                for m in range(1, M + 1):
                    dp[n][k][m] += dp[n - 1][k][m] * m
                    dp[n][k][m] += sum(dp[n - 1][k - 1][1: m])

        # Sum all possible maximum value as result.
        return sum(dp[N][K][1:]) % (10 ** 9 + 7)
