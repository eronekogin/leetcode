"""
https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/
"""


from bisect import bisect_left
from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def max_points(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        """
        max points
        """
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        vals = []

        while heap:
            curr, r, c = heappop(heap)
            vals.append(curr)

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heappush(heap, (grid[nr][nc], nr, nc))

        max_val = -1
        for i, val in enumerate(vals):
            max_val = max(max_val, val)
            vals[i] = max_val

        return [
            bisect_left(vals, q)
            for q in queries
        ]
