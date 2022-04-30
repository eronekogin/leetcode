"""
https://leetcode.com/problems/sort-integers-by-the-power-value/
"""


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_power(x: int) -> int:
            if x not in memo:
                if x & 1:
                    memo[x] = 1 + get_power(3 * x + 1)
                else:
                    memo[x] = 1 + get_power(x >> 1)

            return memo[x]

        memo = {1: 0}
        return sorted(
            range(lo, hi + 1),
            key=lambda x: get_power(x)
        )[k - 1]
