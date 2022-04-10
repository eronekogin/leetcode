"""
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
"""


class Solution:
    def findIntegers(self, num: int) -> int:
        dp = [0] * 32
        dp[0], dp[1] = 1, 2
        for i in range(2, 32):
            dp[i] = dp[i - 2] + dp[i - 1]

        k, rslt, preBit = 30, 0, 0
        while k >= 0:
            if num & (1 << k):
                rslt += dp[k]
                if preBit:  # Found consecutive 11, skip the remaining check.
                    return rslt

                preBit = 1
            else:
                preBit = 0

            k -= 1

        return rslt + 1  # The input number itself is a valid number.
