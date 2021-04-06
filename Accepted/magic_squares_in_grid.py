"""
https://leetcode.com/problems/magic-squares-in-grid/
"""


class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        def is_candidate(r: int, c: int) -> bool:
            # Check if the current cell is a possible grid center.
            if r < 1 or r > R - 2 or c < 1 or c > R - 2:
                return False

            rows, cols = [r - 1, r, r + 1], [c - 1, c, c + 1]

            # Check if all the cells in the current grid contains 1 to 9.
            if {grid[nr][nc] for nr in rows for nc in cols} != VALID_DIGITS:
                return False

            # Check if each sum equals to 15.
            for nr in rows:  # Check row.
                if sum(grid[nr][nc] for nc in cols) != 15:
                    return False

            for nc in cols:  # Check column.
                if sum(grid[nr][nc] for nr in rows) != 15:
                    return False

            # Check diagonals.
            if grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1] != 15 or \
                    grid[r + 1][c - 1] + grid[r][c] + grid[r - 1][c + 1] != 15:
                return False

            return True

        VALID_DIGITS = set(range(1, 10))
        R, C = len(grid), len(grid[0])
        cnt = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 5 and is_candidate(r, c):
                    cnt += 1

        return cnt


print(Solution().numMagicSquaresInside(
    [
        [2, 7, 6],
        [1, 5, 9],
        [4, 3, 8]
    ]))
