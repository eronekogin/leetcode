"""
https://leetcode.com/problems/valid-tic-tac-toe-state/
"""


from collections import Counter


class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        def is_winner(t: str) -> bool:
            # Check rows.
            for row in board:
                if all(w == t for w in row):
                    return True

            # Check columns.
            for c in range(N):
                if all(board[r][c] == t for r in range(N)):
                    return True

            # Check diagonals.
            if all(
                    board[r][c] == t
                    for r in range(N)
                    for c in range(N)
                    if r == c):
                return True

            if all(
                    board[r][c] == t
                    for r in range(N)
                    for c in range(N)
                    if r + c == N - 1):
                return True

            return False

        N = len(board)
        cnt = Counter()
        for row in board:
            cnt += Counter(row)

        if cnt['O'] > cnt['X']:  # The first player must place 'X'.
            return False

        if cnt['X'] - cnt['O'] > 1:  # Two players take turns to place chars.
            return False

        xWin, oWin = is_winner('X'), is_winner('O')
        if xWin and oWin:
            return False

        if xWin:
            if cnt['X'] != cnt['O'] + 1:
                return False

        if oWin:
            if cnt['X'] != cnt['O']:
                return False

        return True


print(Solution().validTicTacToe([
    "OXX",
    "XOX",
    "OXO"]))
