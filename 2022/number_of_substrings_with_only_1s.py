"""
https://leetcode.com/problems/number-of-substrings-with-only-1s/
"""


class Solution:
    def numSub(self, s: str) -> int:
        pivots = [-1] + [i for i, c in enumerate(s) if c == '0'] + [len(s)]
        return sum(
            # n = (b - 1 - (a + 1)) / 1 + 1 = b - a - 1
            # number of sub strings between a and b is (n + 1) * n / 2
            ((b - a - 1) * (b - a)) >> 1
            for a, b in zip(pivots, pivots[1:])
        ) % (10 ** 9 + 7)
