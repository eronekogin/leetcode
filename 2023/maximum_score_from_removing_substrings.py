"""
https://leetcode.com/problems/maximum-score-from-removing-substrings/
"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            return self.maximumGain(s[::-1], y, x)

        a, b, rslt = 0, 0, 0
        for c in s:
            if c == 'a':
                a += 1
            elif c == 'b':
                if a > 0:
                    rslt += x  # match ab
                    a -= 1
                else:
                    b += 1  # No leading a.
            else:  # Other chars.
                rslt += min(a, b) * y
                a, b = 0, 0

        return rslt + min(a, b) * y
