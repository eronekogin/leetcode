"""
https://leetcode.com/problems/number-of-orders-in-the-backlog/
"""


from heapq import heappush, heappop


class Solution:
    def getNumberOfBacklogOrders(self, orders: list[list[int]]) -> int:
        buyOrderHeap = []
        sellOrderHeap = []
        for price, amount, type in orders:
            if type == 0:  # buy order
                remainAmount = amount
                while remainAmount > 0 and sellOrderHeap and sellOrderHeap[0][0] <= price:
                    sellPrice, sellAmount = heappop(sellOrderHeap)
                    if remainAmount >= sellAmount:
                        remainAmount -= sellAmount
                    else:
                        sellAmount -= remainAmount
                        remainAmount = 0
                        heappush(sellOrderHeap, (sellPrice, sellAmount))

                if remainAmount > 0:
                    heappush(buyOrderHeap, (-price, remainAmount))
            else:  # sell order
                remainAmount = amount
                while remainAmount > 0 and buyOrderHeap and -buyOrderHeap[0][0] >= price:
                    buyPrice, buyAmount = heappop(buyOrderHeap)
                    if remainAmount >= buyAmount:
                        remainAmount -= buyAmount
                    else:
                        buyAmount -= remainAmount
                        remainAmount = 0
                        heappush(buyOrderHeap, (buyPrice, buyAmount))

                if remainAmount > 0:
                    heappush(sellOrderHeap, (price, remainAmount))

        return (
            sum(x[1] for x in buyOrderHeap) +
            sum(x[1] for x in sellOrderHeap)
        ) % (10 ** 9 + 7)


print(Solution().getNumberOfBacklogOrders(
    [[27, 7, 1], [6, 27, 0], [13, 7, 1], [4, 7, 1], [19, 7, 1], [4, 22, 1], [10, 17, 1], [1, 11, 1], [29, 10, 0], [6, 7, 1]]))
