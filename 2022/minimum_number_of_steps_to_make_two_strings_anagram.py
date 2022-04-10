"""
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
"""


from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cntS = Counter(s)
        cntT = Counter(t)
        return sum((cntS - cntT).values())
