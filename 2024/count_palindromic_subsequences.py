"""
https://leetcode.com/problems/count-palindromic-subsequences/description/
"""


class Solution:
    """
    Solution
    """

    def count_palindromes(self, s: str) -> int:
        """
        count palindromes
        """
        mod = 10 ** 9 + 7
        n = len(s)
        offset = ord('0')

        # Count prefix.
        prefixes = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        freqs = [0] * 10
        for i in range(n):
            digit = ord(s[i]) - offset
            if i > 0:
                for j in range(10):
                    for k in range(10):
                        prefixes[i][j][k] = prefixes[i - 1][j][k]

                        # If the current digit is also k, we need to add
                        # how many j exists before the current index.
                        if k == digit:
                            prefixes[i][j][k] += freqs[j]

            freqs[digit] += 1

        # Count suffix.
        suffixes = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        freqs = [0] * 10
        for i in range(n - 1, -1, -1):
            digit = ord(s[i]) - offset
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suffixes[i][j][k] = suffixes[i + 1][j][k]

                        # If the current digit is also k, we need to add
                        # how many j exists after the current index.
                        if k == digit:
                            suffixes[i][j][k] += freqs[j]

            freqs[digit] += 1

        rslt = 0
        for i in range(2, n - 2):
            for j in range(10):
                for k in range(10):
                    rslt += prefixes[i - 1][j][k] * suffixes[i + 1][j][k]

        return rslt % mod
