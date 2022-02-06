"""
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
"""


class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        board = [[0] * 3 for _ in range(3)]

        # Build final board.
        player = 1
        for r, c in moves:
            board[r][c] = player
            player *= -1

        for row in board:
            if sum(row) == 3:
                return 'A'
            elif sum(row) == -3:
                return 'B'

        for col in zip(*board):
            if sum(col) == 3:
                return 'A'
            elif sum(col) == -3:
                return 'B'

        diagonal = sum([board[0][0], board[1][1], board[2][2]])
        if diagonal == 3:
            return 'A'
        elif diagonal == -3:
            return 'B'

        diagonal = sum([board[2][0], board[1][1], board[0][2]])
        if diagonal == 3:
            return 'A'
        elif diagonal == -3:
            return 'B'

        if len(moves) < 9:
            return 'Pending'
        else:
            return 'Draw'


print(Solution().tictactoe(
    [[2, 0], [1, 1], [0, 2], [2, 1], [1, 2], [1, 0], [0, 0], [0, 1]]))
