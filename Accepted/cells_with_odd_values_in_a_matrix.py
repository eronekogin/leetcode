"""
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
"""


class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        """
        Simply count the odd number of rows and odd number of cols, then for
        m - rowSum stands for each row with even operations, then 
        (m - rowSum) * colSum stands for the odd numbers occur on those (r, c)
        pairs.
        """
        rowCnt, colCnt = [0] * m, [0] * n
        for r, c in indices:
            rowCnt[r] ^= 1
            colCnt[c] ^= 1

        rowSum, colSum = sum(rowCnt), sum(colCnt)
        return (m - rowSum) * colSum + (n - colSum) * rowSum
