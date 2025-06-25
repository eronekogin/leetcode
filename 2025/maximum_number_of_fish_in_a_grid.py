"""
https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/
"""


from collections import deque


class Solution:
    """
    Solution
    """

    def find_max_fish(self, grid: list[list[int]]) -> int:
        """
        find max fish
        """
        def bfs(r: int, c: int) -> int:
            curr_fishes = 0
            queue = deque([(r, c)])
            visited.add((r, c))
            while queue:
                cr, cc = queue.popleft()
                curr_fishes += grid[cr][cc]
                for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        (nr, nc) not in visited and
                        grid[nr][nc] > 0
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

            return curr_fishes

        max_fishes = 0
        visited: set[tuple[int, int]] = set()
        m, n = len(grid), len(grid[0])
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if (r, c) not in visited and v > 0:
                    max_fishes = max(max_fishes, bfs(r, c))

        return max_fishes


print(Solution().find_max_fish([[8, 6], [2, 6]]))
