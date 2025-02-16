"""
https://leetcode.com/problems/count-anagrams/description/
"""


from collections import Counter
from functools import cache, reduce
from math import factorial


class Solution:
    """
    Solution
    """

    def count_anagrams(self, s: str) -> int:
        """
        count anagrams
        """
        @cache
        def get_factorial(x: int) -> int:
            return factorial(x)

        def count_single_word(w: str) -> int:
            n = get_factorial(len(w))
            for v in Counter(w).values():
                n //= get_factorial(v)

            return n % m

        m = 10 ** 9 + 7
        return reduce(lambda x, y: x * count_single_word(y), s.split(), 1) % m
