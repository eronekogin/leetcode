"""
https://leetcode.com/problems/stock-price-fluctuation/
"""


from heapq import heappush, heappop


class StockPrice:
    """
    StockPrice
    """

    def __init__(self):
        self.stocks: dict[int, int] = {}
        self.latest_timestamp: int = 0
        self.min_prices: list[tuple[int, int]] = []
        self.max_prices: list[tuple[int, int]] = []

    def _check_price(self, prices: list[tuple[int, int]], direction: int):
        """
        Find a price from the target heap that is not updated.
        """
        p, t = heappop(prices)
        while p * direction != self.stocks[t]:
            p, t = heappop(prices)

        heappush(prices, (p, t))
        return p * direction

    def update(self, timestamp: int, price: int) -> None:
        """
        Update stock price at a timestamp
        """
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        self.stocks[timestamp] = price
        heappush(self.max_prices, (-price, timestamp))
        heappush(self.min_prices, (price, timestamp))

    def current(self) -> int:
        """
        Get the latest stock price.
        """
        return self.stocks[self.latest_timestamp]

    def maximum(self) -> int:
        """
        Get the maximum price.
        """
        return self._check_price(self.max_prices, -1)

    def minimum(self) -> int:
        """
        Get the minimum price.
        """
        return self._check_price(self.min_prices, 1)
