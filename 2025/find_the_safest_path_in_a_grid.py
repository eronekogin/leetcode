"""
https://leetcode.com/problems/find-the-safest-path-in-a-grid/description/
"""


from collections import deque
from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def maximum_safeness_factor(self, grid: list[list[int]]) -> int:
        """
        maximum safeness factor
        """
        theif_queue = deque()
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 1:
                    theif_queue.append((r, c))
                    grid[r][c] = 0
                else:
                    grid[r][c] = -1

        n = len(grid)

        # Calculate the safeness factor for each cell
        while theif_queue:
            curr_theives = len(theif_queue)
            while curr_theives > 0:
                r, c = theif_queue.popleft()
                v = grid[r][c]

                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == -1:
                        grid[nr][nc] = v + 1
                        theif_queue.append((nr, nc))

                curr_theives -= 1

        heap = [(-grid[0][0], 0, 0)]
        grid[0][0] = -1

        while heap:
            safeness, r, c = heappop(heap)

            if r + 1 == n and c + 1 == n:
                return -safeness

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != -1:
                    heappush(heap, (-min(-safeness, grid[nr][nc]), nr, nc))
                    grid[nr][nc] = -1

        return -1
