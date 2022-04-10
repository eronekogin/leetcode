"""
https://leetcode.com/problems/detect-capital/
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = 0
        for c in word:
            if c.isupper():
                capitals += 1

        if not capitals or capitals == len(word) or (
                capitals == 1 and word[0].isupper()):
            return True

        return False
