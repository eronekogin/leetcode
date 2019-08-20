"""
https://leetcode.com/problems/unique-paths-ii/
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        maxRow, maxCol = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        board = [[0] * (maxCol + 1) for _ in range(maxRow + 1)]
        # Check obstacles in the maxRow and maxCol.
        for row in range(maxRow, -1, -1):
            if obstacleGrid[row][maxCol]:
                break

            board[row][maxCol] = 1

        for col in range(maxCol, -1, -1):
            if obstacleGrid[maxRow][col]:
                break

            board[maxRow][col] = 1

        for col in range(maxCol - 1, -1, -1):
            for row in range(maxRow - 1, -1, -1):
                if obstacleGrid[row][col]:
                    board[row][col] = 0
                else:
                    board[row][col] = board[row + 1][col] + board[row][col + 1]

        return board[0][0]


obstacleGrid = [
    [0, 1]
]

print(Solution().uniquePathsWithObstacles(obstacleGrid))
