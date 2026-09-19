"""
https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/description/
"""


from itertools import product


class Solution:
    """
    Solution
    """

    def minimum_cost(self, m: int, n: int, h: list[int], v: list[int]) -> int:
        """
        minimum cost
        """
        return sum(h) + sum(v) + sum(map(min, product(h, v)))
