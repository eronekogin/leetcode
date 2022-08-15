"""
https://leetcode.com/problems/shuffle-string/
"""


class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        newChars: list[str] = [None] * len(s)
        for i, c in enumerate(s):
            newChars[indices[i]] = c

        return ''.join(newChars)
