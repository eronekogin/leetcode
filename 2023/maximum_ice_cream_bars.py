"""
https://leetcode.com/problems/maximum-ice-cream-bars/
"""


from collections import Counter


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        cnt = Counter(costs)
        maxCost = max(cnt.keys())
        currCoins = coins
        rslt = 0

        for cost in range(1, maxCost + 1):
            if cnt[cost] == 0:
                continue

            if currCoins < cost:
                break

            newIceCreams = min(cnt[cost], currCoins // cost)
            rslt += newIceCreams
            currCoins -= newIceCreams * cost

        return rslt
