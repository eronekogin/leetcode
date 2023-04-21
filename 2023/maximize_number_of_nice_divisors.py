"""
https://leetcode.com/problems/maximize-number-of-nice-divisors/
"""


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10 ** 9 + 7
        if primeFactors <= 3:
            return primeFactors

        r = primeFactors % 3
        if r == 0:
            return pow(3, primeFactors // 3, MOD)

        if r == 1:
            return (pow(3, (primeFactors - 4) // 3, MOD) * 4) % MOD

        return (pow(3, primeFactors // 3, MOD) * 2) % MOD
