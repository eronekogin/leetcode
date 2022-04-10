"""
https://leetcode.com/problems/stone-game-ii/
"""


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        """
        Suppose dp[i, m] stands for the maximum stones the current player can
        get from piles[i:] with max boarder as 2m, then suppose the first
        player could get x piles, his stone will be dp[i, x], while the
        second player could get dp[x + 1, max(m, x)]. We want the first player
        to get maximum stones, so that we need the second player to have
        minimum stones.
        """
        def dp(i: int, m: int) -> int:
            if (i, m) not in memo:
                if i + (m << 1) >= N:
                    return prefixSum[i]

                memo[(i, m)] = prefixSum[i] - min(
                    dp(i + x, max(x, m))
                    for x in range(1, (m << 1) + 1)
                )

            return memo[(i, m)]

        N = len(piles)
        prefixSum = [0] * (N - 1) + [piles[-1]]
        for i in range(N - 2, -1, -1):
            prefixSum[i] += piles[i] + prefixSum[i + 1]

        memo = {}
        return dp(0, 1)
