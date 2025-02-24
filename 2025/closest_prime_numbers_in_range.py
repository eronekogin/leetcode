"""
https://leetcode.com/problems/closest-prime-numbers-in-range/description/
"""


class Solution:
    """
    Solution
    """

    def closest_primes(self, left: int, right: int) -> list[int]:
        """
        closest primes
        """
        right += 1
        primes: list[int] = [True] * right
        primes[0] = False
        primes[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            for j in range(i * i, right, i):
                primes[j] = False

        candidates = [
            i
            for i, p in enumerate(primes)
            if p and left <= i <= right
        ]

        if len(candidates) < 2:
            return [-1, -1]

        return list(
            min(
                zip(candidates, candidates[1:]),
                key=lambda x: x[1] - x[0]
            )
        )


print(Solution().closest_primes(19, 31))
