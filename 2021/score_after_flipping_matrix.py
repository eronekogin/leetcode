"""
https://leetcode.com/problems/score-after-flipping-matrix/
"""


class Solution:
    def matrixScore(self, A: list[list[int]]) -> int:
        """
        1. For each row, row[0] is the most significant digit and if it is
            1, it could add (1 << (C - 1)) score to the final score. So in
            order to get the maximum score, we must turn the first item in
            each row as 1.
        2. Then for each column, the c th column could add (1 << (C - 1 - c))
            points to the final score.
            2.1 Notice that the if A[r][c] == A[r][0] in the first place, if
                we turn A[r][0], the A[r][c] will be turned as well.
            2.2 So we check how many items in the current column has the same
                value as the first value initially, and we could check if
                we could get more 1s by flipping the current column.
        """
        R, C = len(A), len(A[0])
        rslt = (1 << (C - 1)) * R
        for c in range(1, C):
            curr = sum(A[r][c] == A[r][0] for r in range(R))
            rslt += max(curr, R - curr) * (1 << (C - 1 - c))

        return rslt
