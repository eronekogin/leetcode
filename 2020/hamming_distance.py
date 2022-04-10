"""
https://leetcode.com/problems/hamming-distance/
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        curr = x ^ y
        rslt = 0
        while curr:
            curr, remain = divmod(curr, 2)
            rslt += remain == 1

        return rslt
