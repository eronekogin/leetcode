"""
https://leetcode.com/problems/harshad-number/description/
"""


class Solution:
    """
    Solution
    """

    def sum_of_the_digits_of_harshad_number(self, x: int) -> int:
        """
        sum of the digits of harshed number
        """
        digits_sum = 0
        curr = x
        while curr:
            curr, r = divmod(curr, 10)
            digits_sum += r

        if x % digits_sum == 0:
            return digits_sum

        return -1
