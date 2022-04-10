"""
https://leetcode.com/problems/factorial-trailing-zeroes/
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        rslt, num = 0, n
        while num:  # Keep checking // 5, n // 5 ** 2, n // 5 ** 3...
            num //= 5
            rslt += num

        return rslt
