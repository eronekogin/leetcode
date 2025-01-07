"""
https://leetcode.com/problems/number-of-beautiful-partitions/description/
"""

from functools import cache


class Solution:
    """
    Solution
    """

    def beautiful_partitions(self, s: str, k: int, min_length: int) -> int:
        """
        beautiful partitions
        """
        @cache
        def dp(i: int, is_start: bool, k: int) -> int:
            if i == n:
                return int(k == 0)

            if i > n or k == 0 or (s[i] not in primes and is_start):
                return 0

            if s[i] in primes:
                if is_start:
                    return dp(i + min_length - 1, False, k)

                return dp(i + 1, False, k)

            return (dp(i + 1, True, k - 1) + dp(i + 1, False, k)) % m

        n = len(s)
        primes = '2357'
        if k * min_length > n or s[0] not in primes or s[-1] in primes:
            return 0

        m = 10 ** 9 + 7
        return dp(0, True, k)
