"""
https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/
"""


from math import inf


class Solution:
    """
    Solution
    """

    def min_valid_strings(self, words: list[str], target: str) -> int:
        """
        min valid strings
        """
        trie = {}
        for w in words:
            curr = trie
            for c in w:
                if c not in curr:
                    curr[c] = {}

                curr = curr[c]

        n = len(target)
        dp = [inf] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            curr = trie
            for j in range(i, n):
                if target[j] not in curr:
                    break

                curr = curr[target[j]]

                dp[i] = min(dp[i], 1 + dp[j + 1])

        if dp[0] < inf:
            return int(dp[0])

        return -1


print(Solution().min_valid_strings(
    ["abcdef"], "xyz"))
