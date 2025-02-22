"""
https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/
"""


class Solution:
    """
    Solution
    """

    def distinct_prime_factors(self, nums: list[int]) -> int:
        """
        distinct prime factors
        """
        def count_prime_factors(x: int):
            if x % 2 == 0:
                factors.add(2)
                while x % 2 == 0:
                    x >>= 1

            for i in range(3, int(x ** 0.5) + 1, 2):
                if x % i == 0:
                    factors.add(i)
                    while x % i == 0:
                        x //= i

            if x > 2:
                factors.add(x)

        factors: set[int] = set()
        for x in nums:
            count_prime_factors(x)

        return len(factors)


print(Solution().distinct_prime_factors([27]))
