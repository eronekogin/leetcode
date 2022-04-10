"""
https://leetcode.com/problems/set-matrix-zeroes/
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        maxRow, maxCol = len(matrix), len(matrix[0])
        zeroFlagCol = False
        for row in range(maxRow):
            if not matrix[row][0]:
                zeroFlagCol = True

            for col in range(1, maxCol):
                if not matrix[row][col]:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Set row or col to zeros based on the flag stored at the
        # first element.
        for row in range(1, maxRow):
            for col in range(1, maxCol):
                if not (matrix[row][0] and matrix[0][col]):
                    matrix[row][col] = 0

        # Set the flag row and column.
        if not matrix[0][0]:  # Check row first to prevent overriding the flag.
            for col in range(maxCol):
                matrix[0][col] = 0

        if zeroFlagCol:
            for row in range(maxRow):
                matrix[row][0] = 0


matrix = [
    [1, 1, 1],
    [0, 1, 2]
]
Solution().setZeroes(matrix)
print(matrix)
