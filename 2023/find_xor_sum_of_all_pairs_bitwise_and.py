"""
https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/
"""


from functools import reduce
import operator


class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        """
        (a1 ^ a2) & (b1 ^ b2) = (a1 & b1) ^ (a1 & b2) ^ (a2 & b1) ^ (a2 & b2)
        """
        return reduce(operator.xor, arr1) & reduce(operator.xor, arr2)
