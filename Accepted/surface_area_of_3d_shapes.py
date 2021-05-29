"""
https://leetcode.com/problems/surface-area-of-3d-shapes/
"""


class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        """
        1. If any cell has v cube, then its total surface area is 4 * v + 2.
        2. If it is adjacent to any other cube, the hidden surface area is
            min(adjacent, current) * 2, and we could just subtract it from
            the total surface area.
        """
        area = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v:
                    area += 4 * v + 2

                if r:
                    area -= min(v, grid[r - 1][c]) * 2

                if c:
                    area -= min(v, grid[r][c - 1]) * 2

        return area
