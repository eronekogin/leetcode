"""
https://leetcode.com/problems/number-of-enclaves/
"""


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        R, C = len(grid) - 1, len(grid[0]) - 1

        # Get total numeber of lands and also collect the land on the boundary.
        total = 0
        currLands = []
        for r, row in enumerate(grid):
            for c, isLand in enumerate(row):
                if isLand:
                    total += 1
                    if r == 0 or r == R or c == 0 or c == C:
                        currLands.append((r, c))

        # Try to reach the lands that are not on the boundary.
        visited = set(currLands)
        while currLands:
            nextLands = []
            for r, c in currLands:
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr <= R and 0 <= nc <= C and \
                            (nr, nc) not in visited and grid[nr][nc]:
                        nextLands.append((nr, nc))
                        visited.add((nr, nc))

            currLands = nextLands

        return total - len(visited)
