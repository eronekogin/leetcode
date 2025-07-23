"""
https://leetcode.com/problems/buy-two-chocolates/description/
"""


class Solution:
    """
    Solution
    """

    def buy_choco(self, prices: list[int], money: int) -> int:
        """
        buy choco
        """
        first = second = 200
        for p in prices:
            if p < first:
                first, second = p, first
            elif p < second:
                second = p

        if first + second > money:
            return money

        return money - first - second
