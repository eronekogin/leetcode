"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        Eventually range [m, n] could contain the below special numbers:
        m1: xxx1000...
        n1: xxx0111...
        and m1 & n1 = xxx000...

        So our job is to find all the common bits between m and n and also
        how many bits on the right side of the common bits.
        """
        rightBits = 0
        while m != n:
            m >>= 1
            n >>= 1
            rightBits += 1

        return m << rightBits
