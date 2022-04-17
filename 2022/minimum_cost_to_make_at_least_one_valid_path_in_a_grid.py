"""
https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
"""


from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        """
        1. Suppose there is an edge from a cell to its four neighbors, then
            the weight of the edge is 0 for the directed pointed neighbor and
            1 for the others.
        2. Then the goal is to find the minimum distance from
            (0, 0) to (R - 1, C - 1), we could use dijakstra algorithm then.
        """
        R, C = len(grid), len(grid[0])
        DIRECTIONS = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        heap = [(0, 0, 0)]
        minDistances = defaultdict(lambda: float('inf'))

        while heap:
            minDistance, r, c = heappop(heap)
            if r == R - 1 and c == C - 1:
                return minDistance

            for v, (dr, dc) in DIRECTIONS.items():
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    cost = 1 - (v == grid[r][c])
                    newMinDistance = minDistance + cost
                    if minDistances[(nr, nc)] > newMinDistance:
                        minDistances[(nr, nc)] = newMinDistance
                        heappush(heap, (newMinDistance, nr, nc))


print(Solution().minCost(
    [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))
