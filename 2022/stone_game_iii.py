"""
https://leetcode.com/problems/stone-game-iii/
"""


class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        """
        Suppose dp[i] stands for the highest score alice can win over bob at
        the ith pile when picking first, then we have:
            1. If alice take pile#i, she can win stoneValue[i] - dp[i + 1]
            2. If alice take pile#i and pile#i + 1, she can win
                stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
            3. If alice takes all three piles, she can win
                sum(stoneValue[i: i + 3]) - dp[i + 3]
        So dp[i] is the max outcome among the above three options.

        Since we only need the last three elements in the dp list, we could
        do a bottom up loop instead to save spaces.
        """
        dp = [0] * 3
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(
                sum(stoneValue[i: i + k]) - dp[(i + k) % 3]
                for k in (1, 2, 3)
            )

        if dp[0] == 0:
            return 'Tie'

        if dp[0] > 0:
            return 'Alice'

        return 'Bob'
