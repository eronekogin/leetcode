"""
https://leetcode.com/problems/range-product-queries-of-powers/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def product_queries(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        product queries
        """
        powers: list[int] = []
        curr = n
        while curr:
            p, x = 0, curr
            while x >= 2:
                x >>= 1
                p += 1

            powers.append(p)
            curr -= 1 << p

        powers.sort()
        pre_sums = [0] + list(accumulate(powers))
        mod = 10 ** 9 + 7

        return [
            (1 << (pre_sums[r + 1] - pre_sums[l])) % mod
            for l, r in queries
        ]


print(Solution().product_queries(15, [[0, 1], [2, 2], [0, 3]]))
