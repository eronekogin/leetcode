"""
https://leetcode.com/problems/coin-change-2/
"""


from typing import List


from collections import deque


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [1] + [0] * amount
        for coin in coins:
            for currAmt in range(coin, amount + 1):
                memo[currAmt] += memo[currAmt - coin]

        return memo[-1]
