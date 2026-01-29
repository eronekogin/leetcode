"""
https://leetcode.com/problems/distribute-candies-among-children-i/description/
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
        for x in range(min(n + 1, limit + 1)):
            for y in range(min(n - x + 1, limit + 1)):
                ways += (n - x - y) <= limit

        return ways
