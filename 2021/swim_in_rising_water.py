"""
https://leetcode.com/problems/swim-in-rising-water/
"""


from heapq import heappush, heappop


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        """
        Use Dijkstra's algorithm to find the cells with lowest water to move.

        For example, we could take the original grid as a graph with each cell
        as a node. For grid [[0, 2], [1, 3]], we have four nodes and with four
        edges 0->1, 0->2, 1->3, 2->3. The weight for each edge is the differ on
        the elevation. Then our problem becomes to find the shortest path from
        cell (0, 0) to cell (-1, -1), thus we could apply the Dijkstra's
        algorithm.
        """
        N = len(grid) - 1
        visited = {(0, 0)}
        heap = [(grid[0][0], 0, 0)]
        minTime = 0
        while True:
            t, r, c = heappop(heap)
            minTime = max(minTime, t)
            if r == c == N:
                return minTime

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr <= N and 0 <= nc <= N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heappush(heap, (grid[nr][nc], nr, nc))
