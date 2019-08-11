"""
https://leetcode.com/problems/spiral-matrix/
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:  # List is empty or None.
            return []

        startRow, startCol = 0, 0
        endRow, endCol = len(matrix) - 1, len(matrix[0]) - 1
        rslt = []
        while startRow < endRow and startCol < endCol:
            rslt += matrix[startRow][startCol: endCol]  # Go right.
            rslt += [
                matrix[row][endCol] for row in range(startRow, endRow)
            ]  # Go down.
            rslt += matrix[endRow][endCol: startCol: -1]  # Go left.
            rslt += [
                matrix[row][startCol] for row in range(endRow, startRow, -1)
            ]  # Go up.

            # Go to the next layer.
            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1

        # Collect the remaining ones.
        if startRow == endRow:
            rslt += matrix[startRow][startCol: endCol + 1]
        elif startCol == endCol:
            rslt += [
                matrix[row][startCol] for row in range(startRow, endRow + 1)
            ]

        return rslt


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(Solution().spiralOrder(matrix))
