"""
https://leetcode.com/problems/island-perimeter/
"""


from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        perimeter = 0
        R, C = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(R):
            for c in range(C):
                if grid[r][c]:  # Found a land.
                    for dr, dc in directions:  # Found its boundaries.
                        nr, nc = r + dr, c + dc
                        if nr == -1 or nr == R or nc == -1 or nc == C or\
                                not grid[nr][nc]:
                            perimeter += 1

        return perimeter
