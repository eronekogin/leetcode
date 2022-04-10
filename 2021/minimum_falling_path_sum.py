"""
https://leetcode.com/problems/minimum-falling-path-sum/
"""


class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        N = len(matrix)
        currSum = [0] * N
        for row in matrix:
            nextSum = [0] * N
            for c in range(N):
                nextSum[c] = min(
                    currSum[nc]
                    for nc in [c - 1, c, c + 1]
                    if 0 <= nc < N) + row[c]

            currSum = nextSum

        return min(currSum)


print(Solution().minFallingPathSum([
    [2, 1, 3],
    [6, 5, 4],
    [7, 8, 9]
]))
