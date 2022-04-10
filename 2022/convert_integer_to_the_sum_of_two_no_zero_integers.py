"""
https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
"""


class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        def is_zero_integer(x: int) -> bool:
            return '0' in str(x)

        for x in range(1, (n >> 1) + 1):
            y = n - x
            if not is_zero_integer(x) and not is_zero_integer(y):
                return [x, y]
