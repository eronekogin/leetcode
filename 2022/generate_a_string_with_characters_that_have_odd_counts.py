"""
https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n & 1:
            return 'a' * n
        else:
            half = n >> 1
            if half & 1:
                return 'a' * half + 'b' * half
            else:
                return 'a' * (half - 1) + 'b' * (half + 1)
