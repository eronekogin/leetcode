"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rslt = 0
        for i in range(1, len(prices)):
            rslt += max(prices[i] - prices[i - 1], 0)

        return rslt


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
