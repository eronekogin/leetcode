"""
https://leetcode.com/problems/reverse-bits/
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        num, rslt = n, 0
        for _ in range(32):
            rslt = (rslt << 1) + (num & 1)  # rslt * 2 + last bit of num.
            num >>= 1  # Get the next bit.

        return rslt


print(Solution().reverseBits(43261596))
