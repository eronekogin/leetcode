"""
https://leetcode.com/problems/complement-of-base-10-integer/
"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        """
        Handle the number bit by bit.
        """
        if not N:
            return 1

        curr, i, rslt = N, 0, 0
        while curr:
            rslt += ((curr & 1) ^ 1) << i
            i += 1
            curr >>= 1

        return rslt

    def bitwiseComplement2(self, N: int) -> int:
        """
        Suppose x's complement is y, then x ^ y = z, which contains all ones.
        So if we found the z, then x ^ z = x ^ x ^ y = y.
        """
        allOnes = 1
        while allOnes < N:
            allOnes = (allOnes << 1) + 1

        return allOnes ^ N


print(Solution().bitwiseComplement2(5))
