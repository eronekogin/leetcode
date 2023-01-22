"""
https://leetcode.com/problems/largest-submatrix-with-rearrangements/
"""


class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        rslt = 0
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(C):
                if matrix[r][c] != 0 and r > 0:
                    matrix[r][c] += matrix[r - 1][c]

            sortedRow = sorted(matrix[r], reverse=True)
            for witdth, height in enumerate(sortedRow):
                rslt = max(rslt, height * (witdth + 1))

        return rslt
