"""
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        minDeletedChars = 0
        previousBChars = 0
        for c in s:
            if c == 'a':
                minDeletedChars = min(previousBChars, minDeletedChars + 1)
            else:
                previousBChars += 1

        return minDeletedChars
