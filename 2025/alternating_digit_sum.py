"""
https://leetcode.com/problems/alternating-digit-sum/description/
"""


class Solution:
    """
    Solution
    """

    def alternate_digit_sum(self, n: int) -> int:
        """
        alternate digit sum
        """
        sign = 1
        rslt = 0
        while n:
            n, r = divmod(n, 10)
            rslt += sign * r
            sign *= -1

        return rslt * -1 * sign
