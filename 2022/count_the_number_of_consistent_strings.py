"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        def is_consistent(w: str):
            return set(w).issubset(allowedChars)

        allowedChars = set(allowed)
        return sum(is_consistent(w) for w in words)
