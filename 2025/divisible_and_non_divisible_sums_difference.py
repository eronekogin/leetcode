"""
https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def difference_of_sums(self, n: int, m: int) -> int:
        """
        Docstring for difference_of_sums

        :param self: Description
        :param n: Description
        :type n: int
        :param m: Description
        :type m: int
        :return: Description
        :rtype: int
        """
        not_divisible_sum = 0
        total_sum = 0
        for x in range(1, n + 1):
            if x % m > 0:
                not_divisible_sum += x

            total_sum += x

        return (not_divisible_sum << 1) - total_sum
