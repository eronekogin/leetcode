"""
https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_beautiful_substrings(self, s: str) -> int:
        """
        minimum beautiful substrings
        """
        max_pow = 5 ** 6
        n = len(s)
        dp = [0] + [n + 1] * n

        for start, c in enumerate(s):
            if c != '1':
                continue

            curr = 0
            for end in range(start, n):
                curr = curr * 2 + int(s[end])
                if max_pow % curr == 0:
                    dp[end + 1] = min(dp[end + 1], dp[start] + 1)

        if dp[n] == n + 1:
            return -1

        return dp[n]
