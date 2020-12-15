"""
https://leetcode.com/problems/max-area-of-island/
"""


from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = {
            (r, c)
            for r, row in enumerate(grid)
            for c, v in enumerate(row)
            if v}

        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        R, C = len(grid), len(grid[0])
        maxArea = 0
        while islands:
            currIslands, currArea = [islands.pop()], 1
            while currIslands:
                nextIslands = []
                for r, c in currIslands:
                    for dr, dc in DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and (nr, nc) in islands:
                            islands.remove((nr, nc))
                            nextIslands.append((nr, nc))
                            currArea += 1

                currIslands = nextIslands

            maxArea = max(maxArea, currArea)

        return maxArea


print(Solution().maxAreaOfIsland(
    [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
))
