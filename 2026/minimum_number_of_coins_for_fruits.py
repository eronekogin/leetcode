"""
https://leetcode.com/problems/minimum-number-of-coins-for-fruits/description/
"""


from collections import deque


class Solution:
    """
    Docstring for Solution
    """

    def minimum_coins(self, prices: list[int]) -> int:
        """
        Docstring for minimum_coins

        :param self: Description
        :param prices: Description
        :type prices: list[int]
        :return: Description
        :rtype: int
        """
        queue = deque()
        min_cost = 0

        for i, p in enumerate(prices):
            while queue and queue[0][1] < i:
                queue.popleft()

            min_cost += p

            while queue and queue[-1][0] > min_cost:
                queue.pop()

            queue.append((min_cost, 2 * i + 1))
            min_cost = min(min_cost, queue[0][0])

        return min_cost
