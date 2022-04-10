"""
https://leetcode.com/problems/number-of-closed-islands/
"""


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def flood(r: int, c: int) -> None:
            if 0 <= r < R and 0 <= c < C and grid[r][c] == 0:
                grid[r][c] = 1
                flood(r, c + 1)
                flood(r, c - 1)
                flood(r + 1, c)
                flood(r - 1, c)

        R, C = len(grid), len(grid[0])

        # Flood the islands connected to the boarder first.
        for r in [0, R - 1]:
            for c in range(C):
                if grid[r][c] == 0:
                    flood(r, c)

        for c in [0, C - 1]:
            for r in range(R):
                if grid[r][c] == 0:
                    flood(r, c)

        # Then count the closed island.
        cnt = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    flood(r, c)
                    cnt += 1

        return cnt
