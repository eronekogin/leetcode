"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""


from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:  # Empty matrix.
            return 0

        R, C = len(matrix), len(matrix[0])
        memo = [[0] * C for _ in range(R)]

        def walk(currRow: int, currCol: int) -> int:
            """
            Start from the cell specified by (currRow, currCol) and
            try to walk to its four directions and return the length
            of the longest path it could get.
            """
            if not memo[currRow][currCol]:  # Current cell is not calculated.
                nextMaxLen = 0
                for nextRow, nextCol in [
                    (currRow, currCol - 1), (currRow, currCol + 1),
                        (currRow - 1, currCol), (currRow + 1, currCol)]:
                    if -1 < nextRow < R and -1 < nextCol < C and \
                            matrix[nextRow][nextCol] > matrix[currRow][currCol]:
                        nextMaxLen = max(nextMaxLen, walk(nextRow, nextCol))

                memo[currRow][currCol] = 1 + nextMaxLen

            return memo[currRow][currCol]

        rslt = 0
        for r in range(R):
            for c in range(C):
                rslt = max(rslt, walk(r, c))

        return rslt


matrix = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
print(Solution().longestIncreasingPath(matrix))
