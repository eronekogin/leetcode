"""
https://leetcode.com/problems/battleships-in-a-board/
"""


from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        R, C = len(board), len(board[0])
        cnt = 0
        for r in range(R):
            for c in range(C):
                # Only count the start cell of each battleship. The
                # start cell could be considered as the top left
                # of the battleship, which has no X cell to its left or up.
                if board[r][c] != 'X':
                    continue

                if r > 0 and board[r - 1][c] == 'X':  # Check up side.
                    continue

                if c > 0 and board[r][c - 1] == 'X':  # Check left side.
                    continue

                cnt += 1

        return cnt
