"""
https://leetcode.com/problems/stone-game-v/
"""


class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        N = len(stoneValue)
        dp = [[0] * N for _ in range(N)]
        maxScore = [[0] * N for _ in range(N)]

        # Initialize max score.
        for i in range(N):
            maxScore[i][i] = stoneValue[i]

        # Calculate dp.
        for j in range(1, N):
            m = j
            currSum = stoneValue[j]
            rightHalf = 0

            for i in range(j - 1, -1, -1):
                currSum += stoneValue[i]

                # Calculate next mid.
                while (rightHalf + stoneValue[m]) * 2 <= currSum:
                    rightHalf += stoneValue[m]
                    m -= 1

                if rightHalf * 2 == currSum:
                    dp[i][j] = maxScore[i][m]
                else:
                    dp[i][j] = 0 if i == m else maxScore[i][m - 1]

                dp[i][j] = max(
                    dp[i][j],
                    0 if m == j else maxScore[j][m + 1]
                )

                maxScore[i][j] = max(
                    maxScore[i][j - 1], dp[i][j] + currSum
                )

                maxScore[j][i] = max(
                    maxScore[j][i + 1], dp[i][j] + currSum
                )

        return dp[0][-1]
