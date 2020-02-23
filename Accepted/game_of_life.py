"""
https://leetcode.com/problems/game-of-life/
"""


from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]):
        """
        The below solution are the normal case when the board is not too large.

        Suppose the board is infinite, a possible idea could be:

        In order for us to update a particular cell, we only have to look at
        its 8 neighbors which essentially lie in the row above and below it. 
        So, for updating the cells of a row, we just need the row above and 
        the row below. Thus, we read one row at a time from the file and 
        at max we will have 3 rows in memory. 

        We will keep discarding rows that are processed and then we will keep 
        reading new rows from the file, one at a time.
        """
        neighbors = {
            (r, c) for r in range(-1, 2) for c in range(-1, 2)} - {(0, 0)}

        R, C = len(board), len(board[0])
        for r in range(R):
            for c in range(C):
                liveNeighbors = 0
                for neighbor in neighbors:  # Search for live neighbors.
                    nr, nc = r + neighbor[0], c + neighbor[1]
                    if 0 <= nr < R and 0 <= nc < C and abs(board[nr][nc]) == 1:
                        liveNeighbors += 1

                # Apply rule 1 or 3, mark the original live but now dead cells.
                if board[r][c] == 1 and (
                        liveNeighbors < 2 or liveNeighbors > 3):
                    board[r][c] = -1

                # Apply rule 4, mark the original dead but now live cells.
                if board[r][c] == 0 and liveNeighbors == 3:
                    board[r][c] = 2

        for r in range(R):  # Update board to replace -1 and 2.
            for c in range(C):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
