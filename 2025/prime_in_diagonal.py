"""
https://leetcode.com/problems/prime-in-diagonal/description/
"""

SIZE = 4 * (10 ** 6) + 1
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

    def diagonal_prime(self, nums: list[list[int]]) -> int:
        """
        diagonal prime
        """
        max_prime = 0
        n = len(nums)
        for r in range(n):
            if SIEVE[nums[r][r]]:
                max_prime = max(max_prime, nums[r][r])

            if SIEVE[nums[r][n - r - 1]]:
                max_prime = max(max_prime, nums[r][n - r - 1])

        return max_prime
