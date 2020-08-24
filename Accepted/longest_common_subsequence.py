"""
https://leetcode.com/problems/longest-common-subsequence/
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R, C = len(text1), len(text2)
        memo = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                if text1[r] == text2[c]:
                    memo[r + 1][c + 1] = memo[r][c] + 1
                else:
                    memo[r + 1][c + 1] = max(memo[r][c + 1], memo[r + 1][c])

        return memo[-1][-1]
