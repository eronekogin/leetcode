"""
https://leetcode.com/problems/ugly-number-iii/
"""


from math import gcd


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count_ungly_numbers_less_than(k: int) -> int:
            return (
                k // a + k // b + k // c
                - k // ab - k // ac - k // bc
                + k // abc
            )

        ab = a * b // gcd(a, b)
        ac = a * c // gcd(a, c)
        bc = b * c // gcd(b, c)
        abc = a * bc // gcd(a, bc)
        l, r = 1, 2 * 10 ** 9 + 1
        while l < r:
            m = l + ((r - l) >> 1)
            total = count_ungly_numbers_less_than(m)
            if total >= n:  # Has enough ugly numbers.
                r = m
            else:
                l = m + 1

        return l
