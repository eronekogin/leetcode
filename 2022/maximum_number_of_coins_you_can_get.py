"""
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
"""


class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        sortedPiles = sorted(piles, key=lambda x: -x)
        return sum(
            sortedPiles[i + 1]
            for i in range(0, len(piles) // 3 * 2, 2)
        )
