"""
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
"""


class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        def dfs(r: int, c: int, grid: list[list[int]]) -> None:
            grid[r][c] = land + 1  # Mark as visited.
            for nr, nc in [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1)
            ]:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == land:
                    dfs(nr, nc, grid)

        def count_islands(grid: list[list[int]]) -> int:
            cnt = 0
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == land:
                        dfs(r, c, grid)
                        cnt += 1

            return cnt

        R, C = len(grid), len(grid[0])
        land = 1

        if count_islands(grid) != 1:
            # Either all water cells or already have disconnected islands.
            return 0

        land += 1

        # Try to disconnect the island with one day.
        for r in range(R):
            for c in range(C):
                if grid[r][c] == land:
                    grid[r][c] = 0  # flood the cell with water.
                    if count_islands(grid) != 1:
                        return 1

                    land += 1
                    grid[r][c] = land

        # Otherwise, we just need 2 days to separate any connected island.
        # For example, by adding water to the right and below of the top-left
        # most cell of the island.
        return 2
