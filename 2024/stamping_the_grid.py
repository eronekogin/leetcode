"""
https://leetcode.com/problems/stamping-the-grid/description/
"""


class Solution:
    """
    Solution
    """

    def possible_to_stamp(
        self,
        grid: list[list[int]],
        stamp_height: int,
        stamp_width: int
    ) -> bool:
        """
        possible_to_stamp
        """
        def acc(matrix: list[list[int]]):
            rslt = [[0] * (c + 1) for _ in range(r + 1)]
            for i in range(r):
                for j in range(c):
                    rslt[i][j] = (
                        rslt[i - 1][j] +
                        rslt[i][j - 1] -
                        rslt[i - 1][j - 1] +
                        matrix[i][j]
                    )

            return rslt

        def zone_sum(matrix: list[list[int]], r0: int, c0: int):
            r1 = min(r - 1, r0 + stamp_height - 1)
            c1 = min(c - 1, c0 + stamp_width - 1)
            return (
                matrix[r1][c1] -
                matrix[r1][c0 - 1] -
                matrix[r0 - 1][c1] +
                matrix[r0 - 1][c0 - 1]
            )

        r, c = len(grid), len(grid[0])
        acc_grid = acc(grid)
        stamped_matrix = [[0] * c for _ in range(r)]

        for r0 in range(r - stamp_height + 1):
            r1 = r0 + stamp_height - 1
            for c0 in range(c - stamp_width + 1):
                c1 = c0 + stamp_width - 1
                stamped_matrix[r1][c1] = zone_sum(acc_grid, r0, c0) == 0

        acc_stamp = acc(stamped_matrix)
        for r0 in range(r):
            for c0 in range(c):
                if grid[r0][c0] == 0 and zone_sum(acc_stamp, r0, c0) == 0:
                    return False

        return True
