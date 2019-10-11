"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        currMaxProfit, i, n = 0, 0, len(prices) - 1
        currValley = currPeak = prices[0]
        while i < n:
            while i < n and prices[i] >= prices[i + 1]:  # Searching valley.
                i += 1

            currValley = prices[i]
            while i < n and prices[i] <= prices[i + 1]:  # Searching peak.
                i += 1

            currPeak = prices[i]
            currMaxProfit += currPeak - currValley

        return currMaxProfit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
