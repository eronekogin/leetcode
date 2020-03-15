"""
https://leetcode.com/problems/coin-change/
"""


from typing import List
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp[n] stands for the minimum coins we need in order to be summed as n.
        Then dp[n] = min(dp[n - coins[0]], ..., dp[n - coins[-1]]) + 1.
        when n = 0, dp[0] = 0 as no coins can form 0 amount.
        """
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] < float('inf') else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """
        Use BFS which is to find the shortest path from 0 to amount.
        This is much faster than the above dp solution.
        """
        if not amount:  # Don't need any coin.
            return 0

        queue = deque([(0, 0)])
        visited = [True] + [False] * amount
        while queue:
            totalCoins, currVal = queue.popleft()
            totalCoins += 1  # Take a new coin.
            for coin in coins:
                nextVal = currVal + coin
                if nextVal == amount:  # Find a combination.
                    return totalCoins

                if nextVal < amount:  # Could add more coins.
                    if not visited[nextVal]:  # Current value not checked.
                        visited[nextVal] = True  # Prevent checking again.
                        queue.append((totalCoins, nextVal))

        return -1  # Cannot find any combination.


print(Solution().coinChange2([1, 2, 5], 11))
