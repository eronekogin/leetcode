"""
https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
"""


from collections import Counter
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        cnt = Counter(deck)
        g = gcd(*cnt.values())
        return g > 1
