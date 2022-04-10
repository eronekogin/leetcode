"""
https://leetcode.com/problems/uncrossed-lines/
"""


from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        R, C = len(A), len(B)
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                if A[r] == B[c]:
                    dp[r + 1][c + 1] = dp[r][c] + 1
                else:
                    dp[r + 1][c + 1] = max(dp[r][c + 1], dp[r + 1][c])

        return dp[-1][-1]
