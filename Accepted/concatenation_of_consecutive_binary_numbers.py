"""
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        rslt = 0
        for i in range(1, n + 1):
            rslt = (rslt << (len(bin(i)) - 2)) % MOD + i % MOD

        return rslt % MOD


print(Solution().concatenatedBinary(3))
