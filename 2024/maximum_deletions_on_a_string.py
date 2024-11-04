"""
https://leetcode.com/problems/maximum-deletions-on-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def delete_string(self, s: str) -> int:
        """
        delete string
        """
        n = len(s)

        if len(set(s)) == 1:
            return n

        # longest common string starting at index i and index j.
        lcs = [[0] * (n + 1) for _ in range(n + 1)]

        # Maximum deletions of substring starting at index i.
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    lcs[i][j] = lcs[i + 1][j + 1] + 1

                if lcs[i][j] >= j - i:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[0]
