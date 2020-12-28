"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        1. Suppose notHold[i] is the cashes we have when we are not holding
            any stock at the end of the day i, then we have:
            1.1 If we don't have any stock on the day i - 1 and do nothing on
                the day i, then we have:
                notHold[i] = notHold[i - 1]
            1.2 If we have a stock on the day i - 1 and sell it on the day i,
                then we have:
                notHold[i] = hold[i - 1] + prices[i] - fee

            So notHold[i] = max(notHold[i - 1], hold[i - 1] + prices[i] - fee)

        2. Suppose hold[i] is the cashes we have when we are holding some stock
            at the end of the day i, then we have:
            2.1 If we have some stock on the day i - 1 and do nothing on the
                day i, then we have:
                hold[i] = hold[i - 1]
            2.2 If we don't have any stock on the day i - 1 and buy a new stock
                on the day i, then we have:
                hold[i] = notHold[i - 1] - prices[i]

                Notice that buying a stock does not charge any fee.
            2.3 If we have some stock on the day i - 1, sell it on the day i
                and buy a new stock on the day i, then we have:
                hold[i] = hold[i - 1] + prices[i] - fee - prices[i]
                    = hold[i - 1] - fee

                Notice that this value is already less than 2.1

            So hold[i] = max(hold[i - 1], notHold[i - 1] - prices[i])

        3. Then our goal is to calculate notHold[len(prices) - 1].
        """
        notHold, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            notHold = max(notHold, hold + prices[i] - fee)
            hold = max(hold, notHold - prices[i])

        return notHold
