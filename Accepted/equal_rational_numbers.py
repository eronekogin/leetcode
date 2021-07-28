"""
https://leetcode.com/problems/equal-rational-numbers/
"""

from fractions import Fraction


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        """
        1. Suppose we have a number x = 0.(12), which stands for a repeating
            rational number 0.1212121212..., we could interpret it as
            x = 12/10^2 + 12/10^4 + 12/10^6 + ..., suppose r = 1/10^2, then
            x = 12 * (r + r^2 + r^4 + ...) = 12 * r / (1 - r).
        2. Then suppose the repeating part of x is y and its length is k, then
            the repeating part could be represented as y * r / (1 - r), where
            r = 10^-k.
        3. For the integer part and the non-repeating decimal part, simply
            convert them to a fraction.
        """
        def convert(w: str) -> Fraction:
            if '.' not in w:
                return Fraction(int(w), 1)

            i = w.index('.')
            rslt = Fraction(int(w[:i]), 1)
            w = w[i+1:]
            if '(' not in w:
                if w:
                    rslt += Fraction(int(w), 10 ** len(w))
                return rslt

            i = w.index('(')
            if i:
                rslt += Fraction(int(w[:i]), 10 ** i)
            w = w[i+1:-1]
            j = len(w)
            rslt += Fraction(int(w), 10**i * (10**j - 1))
            return rslt

        return convert(s) == convert(t)
