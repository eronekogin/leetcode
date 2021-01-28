"""
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
"""


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        """
        The below solution simply based on the question's pre-assumptions:

        1. Since R could be no larger than 10**6, which means the binary form
            for any number between L and R is within 20 bits.
        2. This means the total number of 1s could be no more than 20.
        3. Then the prime numbers not greater than 17 are 2, 3, 5, 7, 11, 13,
            17 and 19.
        """
        PRIMES = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(i).count('1') in PRIMES for i in range(L, R + 1))
