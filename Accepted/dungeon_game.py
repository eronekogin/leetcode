"""
https://leetcode.com/problems/dungeon-game/
"""


from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        Use dynamic programming.
        """
        maxRow, maxCol = len(dungeon) - 1, len(dungeon[0]) - 1
        memo = [[1] * (maxCol + 1) for _ in range(maxRow + 1)]

        # Initialize the last row and the last column.
        memo[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for r in range(maxRow - 1, -1, -1):  # Could only go up.
            memo[r][maxCol] = max(1, memo[r + 1][maxCol] - dungeon[r][maxCol])

        for c in range(maxCol - 1, -1, -1):  # Could only go left.
            memo[maxRow][c] = max(1, memo[maxRow][c + 1] - dungeon[maxRow][c])

        # Calculate the remaining items from bottom right to top left.
        for r in range(maxRow - 1, -1, -1):
            for c in range(maxCol - 1, -1, -1):
                memo[r][c] = max(
                    1, min(memo[r + 1][c], memo[r][c + 1]) - dungeon[r][c])

        return memo[0][0]
