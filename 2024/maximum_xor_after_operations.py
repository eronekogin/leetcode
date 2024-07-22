"""
https://leetcode.com/problems/maximum-xor-after-operations/description/
"""


import operator
from functools import reduce


class Solution:
    """
    A[i] & (A[i] ^ x) enable you to turn 1-bit to 0-bit from A[i] since x is arbitrary.
    For an array contains all 1, if the count is even, XOR operation gives you 0, otherwise 1.
    Therefore, the question is equivalent to: if you can convert any digit from 1 to 0 for any number, 
    what is the max for XOR(A[i]).
    The max we can get is of course to make every digit of the answer to be 1 if possible 
    (not if a digit is 0 for all number, there is nothing we can do).  Therefore, OR(A[i]) is an approach.
    """

    def maximum_xor(self, nums: list[int]) -> int:
        """
        maximum xor
        """
        return reduce(operator.ior, nums)
