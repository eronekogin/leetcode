"""
https://leetcode.com/problems/prime-arrangements/
"""


from math import sqrt, factorial


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        isPrimeFlags = [True] * (n + 1)
        for prime in range(2, int(sqrt(n)) + 1):
            if isPrimeFlags[prime]:
                for x in range(prime * prime, n + 1, prime):
                    isPrimeFlags[x] = False

        totalPrimes = sum(isPrimeFlags[2:])
        return (factorial(totalPrimes) * factorial(n - totalPrimes)) % (10 ** 9 + 7)
