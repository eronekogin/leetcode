"""
https://leetcode.com/problems/count-ways-to-make-array-with-product/
"""


from math import comb


class Solution:
    def waysToFillArray(self, queries: list[list[int]]) -> list[int]:
        def calc(n: int, k: int):
            cnt = 1
            for p in PRIMES_UNDER_100:
                r = 0
                while k % p == 0:
                    r += 1
                    k /= p

                cnt *= comb(n - 1 + r, r)

            if k != 1:
                cnt *= n

            return cnt % MOD

        PRIMES_UNDER_100 = (
            2, 3, 5, 7, 11, 13, 17, 19, 23,
            29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97
        )

        MOD = 10 ** 9 + 7

        return [calc(n, k) for n, k in queries]
