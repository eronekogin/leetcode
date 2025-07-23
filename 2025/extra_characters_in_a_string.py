"""
https://leetcode.com/problems/extra-characters-in-a-string/description/
"""


class Trie:
    """
    Trie
    """

    def __init__(self) -> None:
        self.memo = {}

    def add(self, w: str) -> None:
        """
        add a new word
        """
        node = self.memo
        for c in w:
            if c not in node:
                node[c] = {}

            node = node[c]

        node['#'] = True


class Solution:
    """
    Solution
    """

    def min_extra_char(self, s: str, dictionary: list[str]) -> int:
        """
        min extra char
        """
        t = Trie()
        for w in dictionary:
            t.add(w)

        n = len(s)
        dp = [0] * (n + 1)
        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node = t.memo
            for end in range(start, n):
                if s[end] not in node:
                    break

                node = node[s[end]]
                if '#' in node:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]
