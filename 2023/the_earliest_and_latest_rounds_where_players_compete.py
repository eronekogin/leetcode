"""
https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/
"""


from functools import cache


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @cache
        def dp(left: int, right: int, currPlayers: int, currRound: int):
            """
            left stands for the position where the firstPlayer is from the left side.
            right stands for the position where the secondPlayer is from the right side.
            """
            # Make sure the firstPlayer is closer to the head of its side than the secondPlayer.
            if left > right:
                return dp(right, left, currPlayers, currRound)
            
            if left == right:
                candidateRounds.add(currRound)
            
            """
            In the next round, the position of the firstPlayer could be in [1, left]. Suppose on the
            next round, the position of the firstPlayer is i, then the position of the secondPlayer
            could be:
                1. The maximum position of the secondPlayer is right - i, which indicates that the first i players
                    from the right side have lost.
                2. The minimum position of the secondPlayer is left - i + 1, which indicates that the first
                    left - i + 1 players from the left side have lost.
            
            So on the next round the following conditions should match:
                1. The remaining players on the left side of firstPlayer and on the right side of secondPlayer should
                    be greater the previous round's remaining players - currPlayers // 2.
                
                2. The remaining players should also be less or equal than the (currPlayers + 1) // 2, which means
                    between the first player and the second player, there is zero or more players.
            """
            for i in range(1, left + 1):
                for j in range(left - i + 1, right - i + 1):
                    if not (currPlayers + 1) // 2 >= i + j >= left + right - currPlayers // 2:
                        continue

                    dp(i, j, (currPlayers + 1) // 2, currRound + 1)

        candidateRounds = set()
        dp(firstPlayer, n - secondPlayer + 1, n, 1)

        return [min(candidateRounds), max(candidateRounds)]