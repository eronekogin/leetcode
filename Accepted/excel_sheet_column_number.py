"""
https://leetcode.com/problems/excel-sheet-column-number/
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        rslt, n = 0, len(s)
        offset = 1 - ord('A')
        for i, c in enumerate(s):
            rslt += (ord(c) + offset) * 26 ** (n - 1 - i)

        return rslt
