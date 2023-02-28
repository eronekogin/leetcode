"""
https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/
"""


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        w = word1 + word2
        n = len(w)
        dp = [[0] * n for _ in range(n)]
        maxLen = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif w[i] == w[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                    if i < len(word1) and j >= len(word1):
                        # Check if palindrome begins with word1[i]
                        # and ends with word2[j].
                        maxLen = max(maxLen, dp[i][j])
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j - 1]
                    )

        return maxLen
