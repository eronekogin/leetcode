"""
https://leetcode.com/problems/palindrome-partitioning-iv/
"""


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        N = len(s)

        # Pre check if s[i...j] is a palindrome.
        dp = [[False] * N for _ in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(N):
                if i >= j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]

        # Then use three cut to check if each cut is a palindrome.
        for i in range(1, N):
            for j in range(i + 1, N):
                if dp[0][i - 1] and dp[i][j - 1] and dp[j][N - 1]:
                    return True

        return False
