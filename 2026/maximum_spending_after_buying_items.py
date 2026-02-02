"""
https://leetcode.com/problems/maximum-spending-after-buying-items/description/
"""


from heapq import merge
from itertools import count
from operator import mul


class Solution:
    """
    Docstring for Solution
    """

    def max_spending(self, values: list[list[int]]) -> int:
        """
        Everyday we buy the current cheapest item that has not
        been bought before. For example, if a < b,

        case#1: buy a at day d, buy b at d + 1, we have
            ad + b(d + 1) = ad + bd + b

        case#2: buy b at day d, buy a at d + 1, we have
            bd + a(d + 1) = bd + ad + a

        So case#2 < case#1, and we should follow case#1 instead
        to spend more money
        """
        return sum(
            map(
                mul,
                count(1),
                merge(*map(reversed, values))
            )
        )
