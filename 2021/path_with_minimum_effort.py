"""
https://leetcode.com/problems/path-with-minimum-effort/
"""


from typing import List


from heapq import heappush, heappop


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        1. Take each cell as a node and the effort when traveling from one cell
            to another is the weight of the edge connected between those two
            nodes.
        2. Then our goal is to find the shortest path from [0, 0] to [-1, -1].
        3. Here we apply the Dijkstra's algorithm, in which the sum of the
            previous path is actually the maximum effort needed in each edge.
        """
        R, C = len(heights) - 1, len(heights[0]) - 1
        minEfforts = [[float('inf')] * (C + 1) for _ in range(R + 1)]
        heap = [(0, 0, 0)]
        while heap:
            currEffort, r, c = heappop(heap)
            if currEffort <= minEfforts[r][c]:
                if r == R and c == C:  # Reached the end.
                    return currEffort

                h = heights[r][c]
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr <= R and 0 <= nc <= C:
                        newEffort = max(currEffort, abs(heights[nr][nc] - h))
                        if minEfforts[nr][nc] > newEffort:
                            minEfforts[nr][nc] = newEffort
                            heappush(heap, (minEfforts[nr][nc], nr, nc))


print(Solution().minimumEffortPath(
    [
        [1, 2, 3],
        [3, 8, 4],
        [5, 3, 5]
    ]
))
