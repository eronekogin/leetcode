"""
https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def is_possible_to_cut_path(self, grid: list[list[int]]) -> bool:
        """
        is possible to cut path
        """
        m, n = len(grid), len(grid[0])

        # Mark all cells as zero from top to bottom if its preceding cell is zero
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if (r == c == 0) or v == 0:
                    continue

                if (r == 0 or grid[r - 1][c] == 0) and (c == 0 or grid[r][c - 1] == 0):
                    grid[r][c] = 0

        # Mark all cells as zero from bottom to top if its succeding cell is zero
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r == m - 1 and c == n - 1) or grid[r][c] == 0:
                    continue

                if (r == m - 1 or grid[r + 1][c] == 0) and (c == n - 1 or grid[r][c + 1] == 0):
                    grid[r][c] = 0

        cnt = Counter(
            r + c
            for r in range(m)
            for c in range(n)
            if grid[r][c]
        )

        return any(cnt[i] < 2 for i in range(1, n + m - 2))


print(Solution().is_possible_to_cut_path([[1, 1, 1], [1, 0, 0], [1, 1, 1]]))
