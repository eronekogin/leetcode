"""
https://leetcode.com/problems/minimum-path-sum/
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        maxRow, maxCol = len(grid) - 1, len(grid[0]) - 1
        board = [[0] * (maxCol + 1) for _ in range(maxRow + 1)]
        # Calculate the steps on the maxCol and maxRow.
        board[maxRow][maxCol] = grid[maxRow][maxCol]
        for col in range(maxCol - 1, -1, -1):
            board[maxRow][col] = grid[maxRow][col] + board[maxRow][col + 1]

        for row in range(maxRow - 1, -1, -1):
            board[row][maxCol] = grid[row][maxCol] + board[row + 1][maxCol]

        # Calculate the remaining steps on the board.
        for col in range(maxCol - 1, -1, -1):
            for row in range(maxRow - 1, -1, -1):
                board[row][col] = grid[row][col] + min(
                    board[row + 1][col], board[row][col + 1])

        return board[0][0]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(Solution().minPathSum(grid))
