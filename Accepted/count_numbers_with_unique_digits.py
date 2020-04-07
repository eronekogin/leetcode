"""
https://leetcode.com/problems/count-numbers-with-unique-digits/
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:  # n == 0
            return 1  # 0 is the only unique number in [0, 1).

        if n == 1:
            return 10  # All numbers are unique in [0, 10).

        rslt, options = 10, 9
        for i in range(1, n):
            # For the 2nd position, 0 could be one of an option.
            # And the first position takes 1 digit, the remaining ones are
            # 9.
            options *= 10 - i
            rslt += options

        return rslt
