"""
https://leetcode.com/problems/minesweeper/
"""


from typing import List
from collections import deque


class Solution:
    def updateBoard(
            self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        sr, sc = click

        # If click on a mine.
        if board[sr][sc] == 'M':
            board[sr][sc] = 'X'
            return board

        offsets = [
            (dr, dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1]
            if dr or dc]
        R, C = len(board), len(board[0])
        currReveals = deque([(sr, sc)])
        while currReveals:
            r, c = currReveals.popleft()
            mines, toBeRevealed = 0, []
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if -1 < nr < R and -1 < nc < C:
                    if board[nr][nc] == 'M':
                        mines += 1
                    elif board[nr][nc] == 'E':
                        toBeRevealed.append((nr, nc))

            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for nr, nc in toBeRevealed:
                    board[nr][nc] = 'A'  # Mark it with another char.
                    currReveals.append((nr, nc))

        return board


print(Solution().updateBoard(
    [
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'M', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E']], [3, 0]))
