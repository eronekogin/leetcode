"""
https://leetcode.com/problems/get-maximum-in-generated-array/
"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n

        vals = [0, 1] + [None] * (n - 1)
        for val in range(2, n + 1):
            i, r = divmod(val, 2)
            if r:  # val is odd.
                vals[val] = vals[i] + vals[i + 1]
            else:
                vals[val] = vals[i]

        return max(vals)
