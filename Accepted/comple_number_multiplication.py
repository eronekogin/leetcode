"""
https://leetcode.com/problems/complex-number-multiplication/
"""


from typing import Tuple


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def get_integer(s: str) -> Tuple[int, int]:
            x, y = s.split('+')
            return (int(x), int(y[:-1]))

        x1, y1 = get_integer(a)
        x2, y2 = get_integer(b)
        return '+'.join([str(x1 * x2 - y1 * y2), str(x1 * y2 + y1 * x2) + 'i'])
