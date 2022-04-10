"""
https://leetcode.com/problems/number-of-lines-to-write-string/
"""


class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        memo = dict(zip('abcdefghijklmnopqrstuvwxyz', widths))
        lines, lineLen = 1, 0
        for c in s:
            width = memo[c]
            if lineLen + width > 100:
                lines += 1
                lineLen = width
            else:
                lineLen += width

        return [lines, lineLen]
