"""
https://leetcode.com/problems/contain-virus/
"""


from typing import List


class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        def get_curr_regions(r: int, c: int) -> None:
            if (r, c) not in visited:
                visited.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < R and 0 <= nc < C:
                        if grid[nr][nc] == 1:
                            get_curr_regions(nr, nc)
                        elif grid[nr][nc] == 0:
                            neighbors[-1].add((nr, nc))
                            regionLens[-1] += 1

        R, C = len(grid), len(grid[0])
        rslt = 0
        while True:
            visited, regions, neighbors, regionLens = set(), [], [], []
            for r, row in enumerate(grid):
                for c, v in enumerate(row):
                    if v == 1 and (r, c) not in visited:  # Found a new region.
                        regions.append(set())
                        neighbors.append(set())
                        regionLens.append(0)
                        get_curr_regions(r, c)

            if not regions:  # No new infected regions are found.
                break

            # Found the current region that will infect most neighbors.
            # The index is guaranteed to be unique based on the questions'
            # assumption.
            maxIdx = neighbors.index(max(neighbors, key=len))
            rslt += regionLens[maxIdx]

            # Then let the other infected regions infect their neighbors
            # on the next day.
            for i, region in enumerate(regions):
                if i == maxIdx:
                    for r, c in region:
                        grid[r][c] = None  # Mark the blocked cell to None.
                else:
                    for r, c in neighbors[i]:
                        grid[r][c] = 1

        return rslt
