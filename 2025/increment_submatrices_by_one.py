"""
https://leetcode.com/problems/increment-submatrices-by-one/description/
"""


class Solution:
    """
    Solution
    """

    def range_add_queries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        """
        range add queries
        """
        matrix = [[0] * n for _ in range(n)]
        for tr, lc, br, rc in queries:
            for r in range(tr, br + 1):
                matrix[r][lc] += 1
                if rc + 1 < n:
                    matrix[r][rc + 1] -= 1

        for r in range(n):
            for c in range(1, n):
                matrix[r][c] += matrix[r][c - 1]

        return matrix
