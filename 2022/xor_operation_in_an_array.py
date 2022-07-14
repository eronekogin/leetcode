"""
https://leetcode.com/problems/xor-operation-in-an-array/
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        rslt = 0
        for i in range(n):
            rslt ^= start + (i << 1)

        return rslt
