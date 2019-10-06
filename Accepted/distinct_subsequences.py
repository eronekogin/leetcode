"""
https://leetcode.com/problems/distinct-subsequences/
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # dp[i][j] stands for the total distinct subsequence formed
        # by t[0:i] in s[0:j]. Initialize the first row in dp to 1
        # as empty string occurs only once in any string.
        for col in range(n + 1):
            dp[0][col] = 1

        for row in range(m):
            for col in range(n):
                if t[row] != s[col]:
                    # Same as the total sub sequence when not picking the
                    # current character.
                    dp[row + 1][col + 1] = dp[row + 1][col]
                else:
                    # Cound be formed by two cases:
                    # 1. Pick the current char, same as dp[row][col].
                    # 2. Don't pick the current char, which is dp[row + 1][col].
                    dp[row + 1][col + 1] = dp[row][col] + dp[row + 1][col]

        return dp[-1][-1]

    def numDistinct2(self, s: str, t: str) -> int:
        """
        Same idea as the above solution, except that we don't need to store
        all the previous rows but only the lastest previous row, which could
        reduce the space to O(n).
        """
        maxCol, cols = len(s) + 1, range(len(s))
        dp = [1] * maxCol  # dp[0][j] = 1
        for tc in t:
            pre = dp[0]
            dp[0] = 0  # Each new row's first element should have value 0.
            for col in cols:
                temp = dp[col + 1]  # Save dp[row][col] first.
                if tc == s[col]:
                    dp[col + 1] = dp[col] + pre
                else:
                    dp[col + 1] = dp[col]

                pre = temp  # Recover dp[row][col].

        return dp[-1]


s = 'ddd'
t = 'dd'
print(Solution().numDistinct2(s, t))
