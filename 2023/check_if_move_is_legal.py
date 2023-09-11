"""
https://leetcode.com/problems/check-if-move-is-legal/
"""


class Solution:
    def checkMove(self, board: list[list[str]], rMove: int, cMove: int, color: str) -> bool:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            nr, nc = rMove + dr, cMove + dc
            size = 2
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == '.' or (size < 3 and board[nr][nc] == color):
                    break

                if board[nr][nc] == color:
                    return True
                
                nr += dr
                nc += dc
                size += 1
        
        return False
        