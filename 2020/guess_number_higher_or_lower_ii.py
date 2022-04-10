"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/
"""


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
        First of all, this question is to find the minimum cost you need to
        have in order to win this game.

        Then suppose dp[i][j] is the minimum cost we need to guess a number
        in [i, j], and for the first round we guessed the number k, then
        we have:

        1. If k is smaller, our remain guesses will cost dp[k + 1][j].
        2. If k is larger, our remain guesses will cost dp[i][k - 1].
        3. If k is correct, our remain guesses cost 0.

        So the worst cost from the above three cases is:
        k + max(dp[k + 1][j], dp[i][k - 1]).

        Now the minimum cost we need to win this game is to find the minimum
        worst cost when we try to select each number in [i, j] as our first
        guess. So in the end we have:

        dp[i][j] = min([k + max(dp[k + 1][j], dp[i][k - 1]) for k in [i, j]])

        Besides, we don't need to check when the first guess is j because
        the case when the first guess is j - 1 always have less cost.
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Pick the smallest from n - 1 to 1 helps us ignore the dp[i][j]
        # where i > j. Those cases are invalid case and they are already
        # default to zero so that they won't impact the comparison result.
        for smallest in reversed(range(1, n)):
            for largest in range(smallest + 1, n + 1):
                minCost = float('inf')
                for firstGuess in range(smallest, largest):
                    minCost = min(minCost, firstGuess + max(
                        dp[smallest][firstGuess - 1],
                        dp[firstGuess + 1][largest]
                    ))

                dp[smallest][largest] = minCost

        return dp[1][n]


print(Solution().getMoneyAmount(3))
