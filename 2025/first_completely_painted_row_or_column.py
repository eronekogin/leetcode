"""
https://leetcode.com/problems/first-completely-painted-row-or-column/description/
"""


class Solution:
    """
    Solution
    """

    def first_complete_index(self, arr: list[int], mat: list[list[int]]) -> int:
        """
        first complete index
        """
        m, n = len(mat), len(mat[0])
        memo: dict[int, tuple[int, int]] = {}
        row_sums = [0] * m
        col_sums = [0] * n
        for r, row in enumerate(mat):
            for c, v in enumerate(row):
                memo[v] = (r, c)

        for i, v in enumerate(arr):
            r, c = memo[v]
            row_sums[r] += 1
            col_sums[c] += 1

            if row_sums[r] == n or col_sums[c] == m:
                return i

        return -1
