"""
https://leetcode.com/problems/making-a-large-island/
"""


from typing import Iterator


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        def neighbors(r: int, c: int) -> Iterator[tuple[int]]:
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield (nr, nc)

        def mark_island(r: int, c: int) -> int:
            area = 1  # Count the current cell.
            grid[r][c] = mark
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    area += mark_island(nr, nc)

            return area

        N = len(grid)

        # Mark each island first.
        islands = {0: 0}  # {mark: island area}
        mark = 2  # Mark starts with 2.
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:  # Found a new island.
                    islands[mark] = mark_island(r, c)
                    mark += 1

        # Walk through all zero cells and check which island it is connected
        # and determine the largest island after that.
        maxArea = max(islands.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    marks = {grid[nr][nc] for nr, nc in neighbors(r, c)}
                    maxArea = max(
                        maxArea, sum(islands[mark] for mark in marks) + 1)

        return maxArea
