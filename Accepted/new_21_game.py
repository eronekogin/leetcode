"""
https://leetcode.com/problems/new-21-game/
"""


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        """
        1. The player will stop drawing cards when she gets K or more than K
            points, which means the final points she will get is in
            [K, K - 1 + W].
            1.1 So if N >= K + W, the probability is 1.0.
            1.2 If N < K, the probability is 0.0.
            1.3 If K == 0, the probability is 1.0 as she will always gets 0
                points.
        2. Each round the player could only get a point from [1, W], suppose
            dp[k] stands for the probability where she could get k points, then
                dp[k] = dp[k - 1] * (1 / W) + dp[k - 2] * (1 / W) + ...
                    + dp[k - w] * (1 / W)
        3. The above equation is because dp[k - 1] is the probability that
            she could get a k - 1 point, then she just need to draw a 1 from
            the cards in order to get k point, since the probability to draw a
            point from the cards is equally distributed, the final probability
            will be dp[k - 1] * (1 / W).
        4. So we could just maintain a sliding window with size W and
            dp[k] = wsum / W.
        """
        if K == 0 or N >= K + W:
            return 1.0

        dp = [1.0] + [0.0] * N
        wsum = 1.0
        for i in range(1, N + 1):
            dp[i] = wsum / W
            if i < K:
                wsum += dp[i]

            if i >= W:
                wsum -= dp[i - W]

        return sum(dp[K:])
