"""
https://leetcode.com/problems/check-if-it-is-a-good-array/
"""


from math import gcd
from functools import reduce


class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        """
        1. If a % x == 0 and b % x == 0, then we could have
            (pa + qb) % x == 0. And if x > 1, we could not make pa + qb = 1
        2. The question is asking if there is an answer with
            p1 * nums[0] + p2 * nums[1] + ... + p(n-1) * nums[n-1] = 1, so
            we could simply check if the common gcd among the whole nums is
            less than 2. 
        """
        return reduce(gcd, nums) < 2
