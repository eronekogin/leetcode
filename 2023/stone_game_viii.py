"""
https://leetcode.com/problems/stone-game-viii/
"""


from functools import reduce
from itertools import accumulate


class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        """
        Suppose prefix sums p[i] = stones[0] + ... + stones[i], and suppose
        dp[i] is the maximum score difference the player can get when the
        game starts at the ith stone, which means the previous stones from
        0 to i have been merged into one stone at index i.

        Assume the current player tries to merge stones from index j, where
        i < j < N, then the score difference the current player can get is
        p[j] - dp[j]. The player needs to try all j between i and N, so we
        have:
        dp[i] = max(p[j] - dp[j]) for j in (i, N - 2]
        dp[N - 2] = p[N - 1]  # When only two stones are left, the player must take all of them.

        The above can be simplified as:
        dp[i] = max(dp[i + 1], p[i + 1] - dp[i + 1]) for i in [0, N - 2)
        dp[N - 2] = p[N - 1]

        And we need to return dp[0] as the answer.
        """
        return reduce(
            lambda acc, curr: max(acc, curr - acc),
            list(accumulate(stones))[::-1][:-1]
        )
