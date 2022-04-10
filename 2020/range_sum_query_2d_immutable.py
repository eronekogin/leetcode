"""
https://leetcode.com/problems/range-sum-query-2d-immutable/
"""


from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.sums = None
            return

        # Caculate each cumulative sum of each cell towards the cell (0, 0).
        R, C = len(matrix), len(matrix[0])
        sums = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                sums[r + 1][c + 1] =\
                    sums[r + 1][c] + sums[r][c + 1] - sums[r][c] + matrix[r][c]

        self.sums = sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.sums:
            return 0

        return self.sums[row2 + 1][col2 + 1] - self.sums[row1][col2 + 1]\
            - self.sums[row2 + 1][col1] + self.sums[row1][col1]
