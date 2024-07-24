"""
https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/
"""


class Solution:
    """
    Solution
    """

    def check_x_matrix(self, grid: list[list[int]]) -> bool:
        """
        check x matrix
        """
        n = len(grid[0]) - 1
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if r == c or r + c == n:
                    if v == 0:
                        return False
                else:
                    if v != 0:
                        return False

        return True


print(Solution().check_x_matrix(
    [[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]))
