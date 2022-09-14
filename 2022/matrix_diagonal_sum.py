"""
https://leetcode.com/problems/matrix-diagonal-sum/
"""


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        N, currSum = len(mat), 0

        for r, row in enumerate(mat):
            for c, v in enumerate(row):
                if r == c or r + c + 1 == N:
                    currSum += v

        return currSum
