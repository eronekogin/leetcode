"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Suppose dp[i][j] stands for the answer for s1[i:] and s2[j:], then we
        have:

            1. When one of the string is empty, the deleted chars must be
                all the chars from the first string, so we have:
                dp[i][len(s2)] = dp[i + 1][len(s2)] + ord(s1[i])
                dp[len(s1)][j] = dp[len(s1)][j + 1] + ord(s2[j])

            2. When s1[i] == s2[j], we could ignore both current chars:
                dp[i][j] = dp[i + 1][j + 1]

            3. When s1[i] != s2[j], we could either delete one of the current
                chars and choose the minimum path:
                dp[i][j] = min(
                    dp[i + 1][j] + ord[s1[i]], dp[i][j + 1] + ord[s2[j]])
        """
        R, C = len(s1), len(s2)
        dp = [[0] * (C + 1) for _ in range(R + 1)]

        # Calculate base cases.
        for r in range(R - 1, -1, -1):
            dp[r][C] = dp[r + 1][C] + ord(s1[r])

        for c in range(C - 1, -1, -1):
            dp[R][c] = dp[R][c + 1] + ord(s2[c])

        # Calculate answer.
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if s1[r] == s2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = min(
                        dp[r + 1][c] + ord(s1[r]), dp[r][c + 1] + ord(s2[c]))

        return dp[0][0]
