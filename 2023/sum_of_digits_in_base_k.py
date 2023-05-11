"""
https://leetcode.com/problems/sum-of-digits-in-base-k/
"""


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        rslt = 0
        while n:
            n, r = divmod(n, k)
            rslt += r

        return rslt
