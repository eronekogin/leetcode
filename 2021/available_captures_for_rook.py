"""
https://leetcode.com/problems/available-captures-for-rook/
"""


class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        # Find the rook first.
        rookRow = rookCol = None
        for r, row in enumerate(board):
            for c, v in enumerate(row):
                if v == 'R':
                    rookRow, rookCol = r, c
                    break

            if rookRow is not None:
                break

        captures = 0
        for r in range(rookRow - 1, -1, -1):  # Up
            if board[r][rookCol] == 'p':
                captures += 1
                break

            if board[r][rookCol] == 'B':
                break

        for r in range(rookRow + 1, len(board)):  # Down
            if board[r][rookCol] == 'p':
                captures += 1
                break

            if board[r][rookCol] == 'B':
                break

        for c in range(rookCol - 1, -1, -1):  # Left
            if board[rookRow][c] == 'p':
                captures += 1
                break

            if board[rookRow][c] == 'B':
                break

        for c in range(rookCol + 1, len(board[0])):  # Right
            if board[rookRow][c] == 'p':
                captures += 1
                break

            if board[rookRow][c] == 'B':
                break

        return captures
