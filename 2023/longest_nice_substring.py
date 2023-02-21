"""
https://leetcode.com/problems/longest-nice-substring/
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s:
            return ''

        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return max(left, right, key=len)

        return s
