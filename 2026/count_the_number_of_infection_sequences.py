"""
https://leetcode.com/problems/count-the-number-of-infection-sequences/description/
"""


from functools import cache
from itertools import pairwise

MOD = 10 ** 9 + 7


@cache
def fact(x: int) -> int:
    """
    fact
    """
    if x < 2:
        return 1

    return (x * fact(x - 1)) % MOD


@cache
def ifact(x: int) -> int:
    """
    ifact
    """
    return pow(fact(x), -1, MOD)


class Solution:
    """
    Solution
    """

    def number_of_sequence(self, n: int, sick: list[int]) -> int:
        """
        number of sequence
        """
        rslt = (
            fact(n - len(sick)) *
            ifact(sick[0]) *
            ifact(n - sick[-1] - 1)
        ) % MOD

        for group in [b - a - 1 for a, b in pairwise(sick) if b > a + 1]:
            rslt = (rslt * ifact(group)) % MOD
            rslt = (rslt * pow(2, group - 1, MOD)) % MOD

        return rslt
