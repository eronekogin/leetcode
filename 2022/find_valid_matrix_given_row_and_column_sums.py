"""
https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
"""


class Solution:
    def restoreMatrix(
        self,
        rowSum: list[int],
        colSum: list[int]
    ) -> list[list[int]]:
        """
        Suppose r1 = 3 and c1 = 4, then we have:
            totalSum = 3 + r2 + ... + rn = 4 + c2 + ... + cn

        For each cell, its value is restrained by the minumum value of rowSum
        and colSum, so if we pick 3 as the value of a0, then we still have:
            r2 + ... + rn = 1 + c2 + ... + cn

        Then eventually at a cell we will have ri = cj, where we could put
        this value at ai. Then all the remaining cells could be zero.
        """
        R, C = len(rowSum), len(colSum)
        rslt = [[0] * C for _ in range(R)]
        r = c = 0
        while r < R and c < C:
            v = min(rowSum[r], colSum[c])
            rslt[r][c] = v
            rowSum[r] -= v
            colSum[c] -= v
            if rowSum[r] == 0:
                r += 1

            if colSum[c] == 0:
                c += 1

        return rslt
