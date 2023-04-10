"""
https://leetcode.com/problems/second-largest-digit-in-a-string/
"""


class Solution:
    def secondHighest(self, s: str) -> int:
        digits: set[str] = set()
        for c in s:
            if c.isdigit():
                digits.add(c)

        if len(digits) <= 1:
            return -1

        return int(sorted(list(digits))[-2])
