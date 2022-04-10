"""
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        rslt, maxNum, maxLen = 1, 1, 1
        for currNum in range(2, n + 1):
            if currNum > maxNum:
                maxLen += 1
                maxNum = (1 << maxLen) - 1

            rslt = (rslt << maxLen) % MOD + currNum % MOD

        return rslt % MOD


print(Solution().concatenatedBinary(3))
