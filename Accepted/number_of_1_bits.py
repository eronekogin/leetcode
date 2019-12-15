"""
https://leetcode.com/problems/number-of-1-bits/
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        num, rslt = n, 0
        while num:
            if num & 1:
                rslt += 1

            num >>= 1

        return rslt

    def hammingWeight2(self, n: int) -> int:
        """
        As n & (n - 1) will flip out the least significant 1, so it will
        eventually flip all the 1's out. Notice it is slow than the above
        solution, but it is an interesting idea.
        """
        num, rslt = n, 0
        while num:
            rslt += 1
            num &= num - 1

        return rslt
