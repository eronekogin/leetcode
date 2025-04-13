"""
https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def minimum_time(self, grid: list[list[int]]) -> int:
        """
        minimum time
        """
        if grid[0][1] > 1 and grid[1][0] > 1:  # No path to move
            return -1

        m, n = len(grid), len(grid[0])
        visited = set()

        heap = [(grid[0][0], 0, 0)]
        while heap:
            curr_time, r, c = heappop(heap)

            if r + 1 == m and c + 1 == n:
                return curr_time

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    waste_time = 1 - ((grid[nr][nc] - curr_time) % 2)
                    next_time = max(grid[nr][nc] + waste_time, curr_time + 1)
                    heappush(heap, (next_time, nr, nc))

        return -1


print(Solution().minimum_time([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]))
