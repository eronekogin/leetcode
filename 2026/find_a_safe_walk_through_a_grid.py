"""
https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/
"""


from collections import deque
from math import inf


class Solution:
    """
    Solution
    """
    def find_safe_walk(self, grid: list[list[int]], health: int) -> bool:
        """
        find safe walk
        """
        q = deque([(0, 0)])
        m, n = len(grid), len(grid[0])
        d = [[inf] * n for _ in range(m)]
        d[0][0] = grid[0][0]

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                cost = d[r][c] + grid[nr][nc]
                if cost >= health:
                    continue

                if cost < d[nr][nc]:
                    d[nr][nc] = cost
                    if grid[nr][nc] == 0:  # Process short distance node first
                        q.appendleft((nr, nc))
                    else:
                        q.append((nr, nc))

        return False
