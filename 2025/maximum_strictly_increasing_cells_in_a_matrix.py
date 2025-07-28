"""
https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def max_increasing_cells(self, mat: list[list[int]]) -> int:
        """
        max increasing cells
        """
        m, n = len(mat), len(mat[0])
        memo = defaultdict(list)
        for r, row in enumerate(mat):
            for c, v in enumerate(row):
                memo[v].append([r, c])

        dp = [[0] * n for _ in range(m)]
        rows = [0] * m
        cols = [0] * n

        for v in sorted(memo):
            for r, c in memo[v]:
                dp[r][c] = max(rows[r], cols[c]) + 1

            for r, c in memo[v]:
                rows[r] = max(rows[r], dp[r][c])
                cols[c] = max(cols[c], dp[r][c])

        return max(rows + cols)
