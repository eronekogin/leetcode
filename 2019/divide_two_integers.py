"""
https://leetcode.com/problems/divide-two-integers/
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(1 << 31) and divisor == -1:
            """
            When dividend is the minimum int on 32 bits machine (-2^31)
            and the divisor is -1 (1FF...FF), it will result in 2^31 which
            is beyond the maximum int on 32 bits machine. (2^31 - 1), so
            consider it as overflow.
            """
            return (1 << 31) - 1  # 2^31 - 1.

        # Calculate result sign.
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        else:
            sign = 1

        a, b, rslt = abs(dividend), abs(divisor), 0

        while a >= b:  # Convert divide to subtract.
            temp, multiplier = b, 1

            while (a >= temp << 1):  # a >= b * 2.
                temp <<= 1
                multiplier <<= 1

            rslt += multiplier
            a -= temp

        return sign * rslt


print(Solution().divide(10, 3))
