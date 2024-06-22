"""
https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_lines(self, stock_prices: list[list[int]]) -> int:
        """
        minimum lines
        """
        if len(stock_prices) < 3:
            return max(0, len(stock_prices) - 1)

        sorted_stocks = sorted(stock_prices)
        x0, y0 = sorted_stocks[0]
        x1, y1 = sorted_stocks[1]
        cnt = 1
        for i in range(2, len(sorted_stocks)):
            x2, y2 = sorted_stocks[i]

            if (y1 - y0) * (x2 - x0) != (x1 - x0) * (y2 - y0):
                cnt += 1

            x0, y0 = x1, y1
            x1, y1 = x2, y2

        return cnt
