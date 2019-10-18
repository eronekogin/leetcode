"""
https://leetcode.com/problems/surrounded-regions/
"""


from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]):
        """
        Use BFS algorithm.
        """
        if not board or not board[0]:  # Empty board.
            return

        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:  # All elments in the board are on the boarder.
            return

        queue = deque([])
        for r in range(R):
            for c in range(C):
                # Put the boarder 'O' items to queue first.
                if (r in (0, R - 1) or c in (0, C - 1)) and board[r][c] == 'O':
                    queue.append((r, c))

        while queue:
            # For the nodes in the queue, its adjancent 'O's should also not be
            # the candidate to be flipped.
            r, c = queue.popleft()
            if 0 <= r < R and 0 <= c < C and board[r][c] == 'O':
                board[r][c] = 'B'
                queue.extend([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'B':  # Reset 'B's to 'O's.
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'  # Flip the 'O's.


board = [
    list('XXXX'),
    list('XOOX'),
    list('XXOX'),
    list('XOXX')
]
print(Solution().solve(board))
