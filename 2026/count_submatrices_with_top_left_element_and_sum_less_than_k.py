"""
https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/
"""


class Solution:
    """
    Solution
    """

    def count_submatrices(self, grid: list[list[int]], k: int) -> int:
        """
        count submatrices
        """
        n = len(grid[0])
        col_sums = [0] * n
        cnt = 0
        for row in grid:
            row_sum = 0
            for j, v in enumerate(row):
                col_sums[j] += v
                row_sum += col_sums[j]
                if row_sum <= k:
                    cnt += 1

        return cnt
