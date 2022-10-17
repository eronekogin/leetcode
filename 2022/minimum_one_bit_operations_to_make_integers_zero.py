"""
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
"""


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        cnt = 0
        while n:
            cnt = -cnt - (n ^ (n - 1))
            n &= n - 1

        return abs(cnt)
