"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        From Day i - 1 to Day i, the states could be transferred as follows:

        hold -- do nothing -- hold
        hold -- sell -- rest
        sold -- do nothing -- sold
        sold -- buy -- hold
        rest -- do nothing -- sold
        """
        sold, hold, rest = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, sold, rest = max(hold, sold - p), max(sold, rest), hold + p

        return max(sold, rest)
