"""
https://leetcode.com/problems/spiral-matrix-ii/
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startRow = startCol = 0
        endRow = endCol = n - 1
        rslt = [[None] * n for _ in range(n)]
        cnt = 0
        while startRow < endRow and startCol < endCol:
            for i in range(startRow, endCol):  # Right.
                cnt += 1
                rslt[startRow][i] = cnt

            for i in range(startRow, endRow):  # Down.
                cnt += 1
                rslt[i][endCol] = cnt

            for i in range(endCol, startCol, -1):  # Left.
                cnt += 1
                rslt[endRow][i] = cnt

            for i in range(endCol, startCol, -1):  # Up.
                cnt += 1
                rslt[i][startCol] = cnt

            startRow += 1
            endRow -= 1
            startCol += 1
            endCol -= 1

        # Handle remaining.
        if startRow == endRow:
            for i in range(startCol, endCol + 1):
                cnt += 1
                rslt[startRow][i] = cnt
        elif startCol == endCol:
            for i in range(startRow, endRow + 1):
                cnt += 1
                rslt[i][startCol] = cnt

        return rslt


print(Solution().generateMatrix(3))
