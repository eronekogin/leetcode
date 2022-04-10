"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/
"""


from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Suppose dp[i + 1][j + 1] contains the maximum length 
        of the squares whose bottom-right corner is matrix[i][j].
        if matrix[i][j] == 1:
            dp[i + 1][j + 1] = 
                min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1
        else:
            dp[i + 1][j + 1] = 0

        Then the answer for our question will be the sum of dp.
        """
        if not matrix or not matrix[0]:
            return 0

        R, C = len(matrix), len(matrix[0])
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        total = 0
        for r in range(R):
            for c in range(C):
                if matrix[r][c]:
                    dp[r + 1][c + 1] = min(
                        dp[r][c + 1], dp[r + 1][c], dp[r][c]) + 1

                total += dp[r + 1][c + 1]

        return total
