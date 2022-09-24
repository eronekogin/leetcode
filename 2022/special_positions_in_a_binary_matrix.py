"""
https://leetcode.com/problems/special-positions-in-a-binary-matrix/
"""


class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows = [row for row in mat]
        cols = [col for col in zip(*mat)]
        rowsWithSumOne = [r for r, row in enumerate(rows) if sum(row) == 1]
        colsWithSumOne = [c for c, col in enumerate(cols) if sum(col) == 1]
        return sum(mat[r][c] == 1 for r in rowsWithSumOne for c in colsWithSumOne)
