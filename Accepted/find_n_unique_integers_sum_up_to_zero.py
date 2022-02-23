"""
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""


class Solution:
    def sumZero(self, n: int) -> list[int]:
        halfLen = n >> 1
        rslt = list(range(1, halfLen + 1)) + list(range(-1, -halfLen - 1, -1))
        if n & 1:
            return rslt + [0]
        else:
            return rslt
