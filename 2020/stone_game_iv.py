"""
https://leetcode.com/problems/stone-game-iv/
"""


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = [False] * (n + 1)
        for i in range(n + 1):
            if not memo[i]:
                for k in range(1, int((n - i) ** 0.5) + 1):
                    memo[i + k ** 2] = True

        return memo[-1]
