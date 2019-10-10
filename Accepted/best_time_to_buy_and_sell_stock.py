"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        rslt, minPrice = 0, prices[0]
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                rslt = max(rslt, price - minPrice)

        return rslt


prices = [2, 1, 2, 1, 0, 1, 2]
print(Solution().maxProfit(prices))
