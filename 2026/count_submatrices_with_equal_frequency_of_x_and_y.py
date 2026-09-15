"""
https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_submatrices(self, grid: list[list[str]]) -> int:
        """
        number of submatrices
        """
        n = len(grid[0])
        cnt = 0
        col_sums = [0] * n
        col_x_cnts = [0] * n

        for row in grid:
            row_sum = 0
            row_x_cnt = 0

            for c, v in enumerate(row):
                if v == 'X':
                    col_sums[c] += 1
                    col_x_cnts[c] += 1
                elif v == 'Y':
                    col_sums[c] += -1

                row_sum += col_sums[c]
                row_x_cnt += col_x_cnts[c]

                if row_sum == 0 and row_x_cnt > 0:
                    cnt += 1

        return cnt


print(Solution().number_of_submatrices([["X", "Y", "."], ["Y", ".", "."]]))
