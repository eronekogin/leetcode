"""
https://leetcode.com/problems/count-good-triplets/
"""


from itertools import combinations


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        return sum(
            abs(ai - aj) <= a and
            abs(aj - ak) <= b and
            abs(ai - ak) <= c
            for ai, aj, ak in combinations(arr, 3)
        )
