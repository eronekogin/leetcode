"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

See https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1)
and https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
for detail explanation.
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        oneSell = twoSell = 0
        oneBuy = twoBuy = prices[0]
        for price in prices:
            # Keep the minimum price for the first buy.
            oneBuy = min(oneBuy, price)

            # Keep the maximum profit for the first buy.
            oneSell = max(oneSell, price - oneBuy)

            # Keep the minimum price for the second buy. Notice that we need
            # to subtract the profit from the first buy for the real stock
            # price we paid.
            twoBuy = min(twoBuy, price - oneSell)

            # Keep the maximum profit for the second buy.
            twoSell = max(twoSell, price - twoBuy)

        return twoSell


prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
print(Solution().maxProfit(prices))
