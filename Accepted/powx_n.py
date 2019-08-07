"""
https://leetcode.com/problems/powx-n/
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        rslt = 1
        while n:
            if n & 1:  # equals n % 2.
                rslt *= x

            x *= x
            n >>= 1  # Equals n //= 2.

        return rslt


print(Solution().myPow(2.2, 4))
