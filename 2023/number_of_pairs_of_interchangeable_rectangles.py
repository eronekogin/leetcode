"""
https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
"""


from math import gcd
from collections import Counter


class Solution:
    """
    Solution
    """

    def interchangeable_rectangles(self, rectangles: list[list[int]]) -> int:
        """
        interchangeable_rectangles
        """
        cnt = Counter()
        for w, h in rectangles:
            g = gcd(w, h)
            cnt[(w // g, h // g)] += 1

        return sum((v * (v - 1)) >> 1 for v in cnt.values())
