"""
https://leetcode.com/problems/ambiguous-coordinates/
"""

from itertools import product


class Solution:
    def ambiguousCoordinates(self, S: str) -> list[str]:
        def make(w: str) -> list[str]:
            # Case: w == '' or w = '0xxx0'
            if not w or (len(w) > 1 and w[0] == w[-1] == '0'):
                return []

            # Case: w == 'xxx0' or w == '0'
            if w[-1] == '0':
                return [w]

            # Case: w = '0XXX'
            if w[0] == '0':
                return [w[0] + '.' + w[1:]]

            # Other cases, just insert '.' between any position in w.
            return [w] + [w[:i] + '.' + w[i:] for i in range(1, len(w))]

        N = len(S) - 1
        return [
            '({0}, {1})'.format(a, b)
            for i in range(2, N)
            for a, b in product(make(S[1: i]), make(S[i: N]))
        ]


print(Solution().ambiguousCoordinates('(00011)'))
