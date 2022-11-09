"""
https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
"""


from collections import Counter


class Solution:
    def maxProfit(self, inventory: list[int], orders: int) -> int:
        balls = sorted(Counter(inventory).items(), reverse=True) + [(0, 0)]
        totalVal, i, w = 0, 0, 0
        while orders > 0:
            w += balls[i][1]
            currSold = min(orders, w * (balls[i][0] - balls[i + 1][0]))
            q, r = divmod(currSold, w)
            totalVal += (
                w * (q * (balls[i][0] + balls[i][0] - (q - 1))) // 2 +
                r * (balls[i][0] - q)
            )
            orders -= currSold
            i += 1

        return totalVal % (10 ** 9 + 7)
