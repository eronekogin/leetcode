"""
https://leetcode.com/problems/repeated-substring-pattern/
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Suppose s = p * n, then S = (s + s)[1: -1] = 2np - 2 = np (2 - 2 / n).
        Then as n >= 2, S >= np, which means S must contain s.
        """
        return s in (s + s)[1: -1]
