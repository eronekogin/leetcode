"""
https://leetcode.com/problems/orderly-queue/
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """
        1. When k == 1, we could only rotate the whole string.
        2. When k > 1, we could have every permuatation of s in our rotated
            result.
        """
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))

        return ''.join(sorted(s))
