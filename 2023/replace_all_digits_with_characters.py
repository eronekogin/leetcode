"""
https://leetcode.com/problems/replace-all-digits-with-characters/
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: str, x: int):
            if x <= 0:
                return c

            return chr(ord(c) + x)

        chars = list(s)
        for i in range(0, len(s) - 1, 2):
            chars[i + 1] = shift(chars[i], int(chars[i + 1]))

        return ''.join(chars)
