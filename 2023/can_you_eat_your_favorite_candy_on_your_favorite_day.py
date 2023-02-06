"""
https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/
"""


class Solution:
    def canEat(self, candiesCount: list[int], queries: list[list[int]]) -> list[bool]:
        preSums = [0]
        for cnt in candiesCount:
            preSums.append(preSums[-1] + cnt)

        return [
            preSums[t] // c <= d < preSums[t + 1]
            for t, d, c in queries
        ]
