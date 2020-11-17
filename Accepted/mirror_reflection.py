"""
https://leetcode.com/problems/mirror-reflection/
"""


from math import gcd


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        Extend the original box to mutiple boxes in order to simulate the
        reflections as follows (p = 3, q = 2):
            See pics/mirror_reflection.png.

        So in the end the ray will meet the point where ap == bq. The easiest
        match is to set a = q and b = p to match the above equation. Now
        consider the following cases:

            1. q is even:
                1.1 p is odd: meet Corner#0.
                1.2 p could not be even as if p is even, then we could divide
                    2 on both sides of the equation to make p and q both odds.
            2. q is odd:
                1.1 p is odd: meet at Corner#1.
                1.2 p is even: meet at Corner#2.
        """
        # Reduce boths sides sides first until at least one side contains an
        # odd number.
        a, b = q, p
        while not (a & 1 or b & 1):
            a >>= 1
            b >>= 1

        if not a & 1:
            return 0
        elif b & 1:
            return 1
        else:
            return 2

    def mirrorReflection2(self, p: int, q: int) -> int:
        """
        Same idea as the above except to use gcd as the divisor.
        """
        g = gcd(p, q)
        a, b = q // g, p // g
        if not a & 1:
            return 0
        elif b & 1:
            return 1
        else:
            return 2
