"""
https://leetcode.com/problems/simplified-fractions/
"""

from math import gcd


class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        if n == 1:
            return []

        rslt: list[str] = ['1/2']
        for denominator in range(3, n + 1):
            for numerator in range(1, denominator):
                if gcd(numerator, denominator) == 1:
                    rslt.append('{0}/{1}'.format(numerator, denominator))

        return rslt
