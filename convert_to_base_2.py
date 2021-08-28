"""
https://leetcode.com/problems/convert-to-base-2/
"""


class Solution:
    def baseNeg2(self, n: int) -> str:
        rslt = []
        while n:
            rslt.append(n & 1)
            n = -(n >> 1)

        return ''.join([str(i) for i in reversed(rslt)] or ['0'])
