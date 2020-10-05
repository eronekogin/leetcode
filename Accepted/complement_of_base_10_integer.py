"""
https://leetcode.com/problems/complement-of-base-10-integer/
"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if not N:
            return 1

        curr, i, rslt = N, 0, 0
        while curr:
            rslt += ((curr & 1) ^ 1) << i
            i += 1
            curr >>= 1

        return rslt


print(Solution().bitwiseComplement(5))
