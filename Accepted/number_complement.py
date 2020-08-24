"""
https://leetcode.com/problems/number-complement/
"""


class Solution:
    def findComplement(self, num: int) -> int:
        curr, rslt, offset = num, 0, 0
        while curr:
            curr, rem = divmod(curr, 2)
            if not rem:
                rslt += 1 << offset

            offset += 1

        return rslt
