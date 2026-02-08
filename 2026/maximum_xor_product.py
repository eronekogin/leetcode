"""
https://leetcode.com/problems/maximum-xor-product/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def maximum_xor_product(self, a: int, b: int, n: int) -> int:
        """
        Docstring for maximum_xor_product

        :param self: Description
        :param a: Description
        :type a: int
        :param b: Description
        :type b: int
        :param n: Description
        :type n: int
        :return: Description
        :rtype: int
        """
        m = 10 ** 9 + 7
        mask = (1 << n) - 1

        # Get different bits between a and b
        d = (a ^ b) & mask

        a = (a | mask) & ~d
        b = (b | mask) & ~d

        if d == 0:  # No different bits
            return (a * b) % m

        highest = 1 << (d.bit_length() - 1)

        return max(
            (a ^ d) * b,
            a * (b ^ d),
            (a ^ d ^ highest) * (b ^ highest),
            (a ^ highest) * (b ^ d ^ highest)
        ) % m
