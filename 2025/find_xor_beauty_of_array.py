"""
https://leetcode.com/problems/find-xor-beauty-of-array/description/
"""


from functools import reduce
from operator import xor


class Solution:
    """
    Solution
    """

    def xor_beauty(self, nums: list[int]) -> int:
        """
        for triplets (i, j, k):
            1. For any i != j, (s[i] | s[j]) & s[k] == (s[j] | s[i]) & s[k], so
                f(i, j, k) ^ f(j, i, k) == 0
            2. For any i == j, (s[i] | s[j]) & s[k] = s[i] & s[k]:
                2.1 For any i != k, s[i] & s[k] == s[k] & s[i], so
                    f(i, j, k) ^ f(j, i, k) == 0
                2.2 For any i == k: s[i] & s[k] == s[i], so f(i, j, k) = s[i]
        """
        return reduce(xor, nums)
