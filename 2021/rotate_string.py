"""
https://leetcode.com/problems/rotate-string/
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A
