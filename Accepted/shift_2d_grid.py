"""
https://leetcode.com/problems/shift-2d-grid/
"""


class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        R, C = len(grid), len(grid[0])
        newGrid = [[0] * C for _ in range(R)]
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                dr, nc = divmod(c + k, C)
                nr = (r + dr) % R
                newGrid[nr][nc] = v

        return newGrid


print(Solution().shiftGrid([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], 1))
