"""
https://leetcode.com/problems/prime-pairs-with-target-sum/description/
"""


SIZE = 10 ** 6 + 1
SIEVE = [1] * SIZE
SIEVE[1] = 0
for i in range(2, int(SIZE ** 0.5) + 1):
    if SIEVE[i]:
        for j in range(i * i, SIZE, i):
            SIEVE[j] = 0


class Solution:
    """
    Solution
    """

    def find_prime_pairs(self, n: int) -> list[list[int]]:
        """
        find prime pairs
        """
        rslt: list[list[int]] = []
        for x in range(2, (n >> 1) + 1):
            y = n - x
            if SIEVE[x] and SIEVE[y]:
                rslt.append([x, y])

        return rslt
