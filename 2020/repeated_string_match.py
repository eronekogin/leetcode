"""
https://leetcode.com/problems/repeated-string-match/
"""


from math import ceil


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        1. Suppose minCnt is the minimum repeating times a needs in order to
            have b as its substring, then len(b) <= minCnt * len(a), which
            means minCnt >= len(b) / len(a).
        2. Suppose q = ceil(len(b) / len(a)):
            2.1 When the repeating time is less than q, the repeated string is
                less than b, which cannont make b as its substring.
            2.2 Check if b in q or q + 1 repeated string of a.
            2.3 For the repeating times greater than q + 1, it does not
                satisfy the minimum repeating condition.
        """
        minCnt = ceil(len(b) / len(a))
        for cnt in [minCnt, minCnt + 1]:
            if b in a * cnt:
                return cnt

        return -1
