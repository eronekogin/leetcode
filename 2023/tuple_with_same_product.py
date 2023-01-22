"""
https://leetcode.com/problems/tuple-with-same-product/
"""


from itertools import combinations
from collections import Counter
from math import comb


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        cnt = Counter(a * b for a, b in combinations(nums, 2))
        return sum(comb(n, 2) * 8 for n in cnt.values() if n > 1)
