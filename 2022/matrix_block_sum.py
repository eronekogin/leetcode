"""
https://leetcode.com/problems/matrix-block-sum/
"""


class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        R, C = len(mat), len(mat[0])

        # Calculate range sum first.
        rangeSum = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                rangeSum[r + 1][c + 1] = (
                    rangeSum[r + 1][c] +
                    rangeSum[r][c + 1] -
                    rangeSum[r][c] +
                    mat[r][c]
                )

        # Then calculate total sum for a specific range.
        rslt = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                r1, c1, r2, c2 = (
                    max(0, r - k),
                    max(0, c - k),
                    min(R, r + k + 1),
                    min(C, c + k + 1)
                )
                rslt[r][c] = (
                    rangeSum[r2][c2] -
                    rangeSum[r2][c1] -
                    rangeSum[r1][c2] +
                    rangeSum[r1][c1]
                )

        return rslt
