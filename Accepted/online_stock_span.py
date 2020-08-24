"""
https://leetcode.com/problems/online-stock-span/
"""


class StockSpanner:

    def __init__(self):
        self.stocks = []  # (stock, days)

    def next(self, price: int) -> int:
        s, cnt = self.stocks, 1
        while s and s[-1][0] <= price:
            cnt += s.pop()[1]

        s.append((price, cnt))
        return cnt
