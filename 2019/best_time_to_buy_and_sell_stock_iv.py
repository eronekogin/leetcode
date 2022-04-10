"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""


from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # No transaction or prices is not long enough to
        # perform one transaction.
        if not k or n < 2:
            return 0

        if k > n // 2:
            return self.no_limit_transaction_max_profit(prices)

        """
        hold[i][j]: The max profit on the jth day with a stock in hand after
            performing at most i transaction.
        
        sold[i][j]: The max profit on the jth day without a stock in hand
            after performing at most i transaction.
        """
        hold = [[0] * n for _ in range(k + 1)]
        sold = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            # You can only buy the stock on the 0th day.
            hold[i][0] = -prices[0]

            for j in range(1, n):
                # Buy the stock on the jth day or not.
                hold[i][j] = max(sold[i - 1][j] - prices[j], hold[i][j - 1])

                # Sell the stock on the jth day or not.
                sold[i][j] = max(hold[i][j - 1] + prices[j], sold[i][j - 1])

        return sold[-1][-1]

    def no_limit_transaction_max_profit(self, prices: List[int]) -> int:
        rslt = 0
        for i in range(1, len(prices)):
            rslt += max(prices[i] - prices[i - 1], 0)

        return rslt


prices = [2, 1, 2, 0, 1]
print(Solution().maxProfit(2, prices))
