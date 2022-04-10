"""
https://leetcode.com/problems/nth-magical-number/
"""


from math import gcd


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """
        1. Suppose l is the least common mutiple of a and b, then for any
            x <= l, if x is a magic number, then x + l is also a magic number.
        2. There are m = l // a + l // b - 1 magic numbers that are less or
            equal to l:
            2.1 l // a of them are divisible by a
            2.2 l // b of them are divisible by b
            2.3 and there is only 1 number, which is l, that is 
                divisible by both a and b.
        3. Then we could just count m:
            3.1 if n could divide m, then there are l * q magical numbers.
            3.2 If the remain is not zero, then we simply count starting from
                a, b, and count towards the end of (r-2)th number by adding
                a or b to the current heads.
        """
        MOD = 10 ** 9 + 7

        l = a // gcd(a, b) * b
        m = l // a + l // b - 1
        q, r = divmod(n, m)

        if r == 0:
            return (l * q) % MOD

        heads = [a, b]
        for _ in range(r - 1):
            if heads[0] < heads[1]:
                heads[0] += a
            else:
                heads[1] += b

        return (q * l + min(heads)) % MOD
