"""
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def minimum_obstacles(self, grid: list[list[int]]) -> int:
        """
        minimum obstacles
        """
        m, n = len(grid), len(grid[0])
        max_removes = m * n + 1
        distance = [[max_removes] * n for _ in range(m)]
        distance[0][0] = grid[0][0]
        heap = [(distance[0][0], 0, 0)]

        while heap:
            d, r, c = heappop(heap)
            if r + 1 == m and c + 1 == n:
                return d

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if m > nr >= 0 <= nc < n and grid[nr][nc] + d < distance[nr][nc]:
                    distance[nr][nc] = grid[nr][nc] + d
                    heappush(heap, (distance[nr][nc], nr, nc))

        return -1


print(Solution().minimum_obstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]]))
