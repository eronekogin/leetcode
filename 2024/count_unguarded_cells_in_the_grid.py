"""
https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/
"""


class Solution:
    """
    Solution
    """

    def count_unguarded(
        self,
        m: int,
        n: int,
        guards: list[list[int]],
        walls: list[list[int]]
    ) -> int:
        """
        count unguarded
        """
        unguarded = [[0] * n for _ in range(m)]

        for r, c in guards:
            unguarded[r][c] = 2

        for r, c in walls:
            unguarded[r][c] = 2

        for r, c in guards:
            # top
            for nr in range(r - 1, -1, -1):
                if unguarded[nr][c] == 2:
                    break

                unguarded[nr][c] = 1

            # bottom
            for nr in range(r + 1, m):
                if unguarded[nr][c] == 2:
                    break

                unguarded[nr][c] = 1

            # left
            for nc in range(c - 1, -1, -1):
                if unguarded[r][nc] == 2:
                    break

                unguarded[r][nc] = 1

            # right
            for nc in range(c + 1, n):
                if unguarded[r][nc] == 2:
                    break

                unguarded[r][nc] = 1

        return sum(v == 0 for row in unguarded for v in row)
