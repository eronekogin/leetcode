"""
https://leetcode.com/problems/count-primes/
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:  # There is no prime less than the current n.
            return 0

        isPrime = [1] * n  # All the non-negative numbers less than n.
        isPrime[0] = isPrime[1] = 0

        # Start from i * i as all the n * i while n < i has all been
        # marked by the previous steps.
        i = 2
        start = i * i
        while start < n:
            if isPrime[i]:
                # Much faster than for j in range(start, n, i): isPrime[j] = 0.
                isPrime[start: n: i] = [0] * ((n - 1 - start) // i + 1)

            i += 1
            start = i * i

        return sum(isPrime)
