"""
https://leetcode.com/problems/abbreviating-the-product-of-a-range/description/
"""

from math import prod
import sys
sys.set_int_max_str_digits(0)


class Solution:
    """
    Solution
    """

    def abbreviate_product(self, left: int, right: int) -> str:
        """
        abbreviate_product
        """
        string = str(prod(list(range(left, right + 1))))
        n_string = string.rstrip("0")
        zeros = len(string) - len(n_string)

        if len(n_string) <= 10:
            return n_string + "e" + str(zeros)
        else:
            return n_string[:5] + "..." + n_string[-5:] + "e" + str(zeros)


print(Solution().abbreviate_product(371, 375))
