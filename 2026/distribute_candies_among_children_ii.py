"""
https://leetcode.com/problems/distribute-candies-among-children-ii/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def distribute_candies(self, n: int, limit: int) -> int:
        """
        Docstring for distribute_candies

        :param self: Description
        :param n: Description
        :type n: int
        :param limit: Description
        :type limit: int
        :return: Description
        :rtype: int
        """
        if 3 * limit < n:
            return 0

        ways = 0
        for x in range(max(0, n - 2 * limit), min(n, limit) + 1):
            ways += min(n - x, limit) - max(0, n - x - limit) + 1

        return ways
