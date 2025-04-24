"""
https://leetcode.com/problems/number-of-ways-to-earn-points/description/
"""


class Solution:
    """
    Solution
    """

    def ways_to_reach_target(self, target: int, types: list[list[int]]) -> int:
        """
        ways to reach target
        """
        # dp[i] stands for number of ways to reach point i.
        # dp[i] can be formed from dp[i - mark], dp[i - mark * 2], ...
        # dp[i - mark * cnt]
        dp = [1] + [0] * target
        m = 10 ** 9 + 7
        for cnt, t in types:
            for i in range(target, -1, -1):
                for k in range(1, min(cnt, i // t) + 1):
                    dp[i] = (dp[i] + dp[i - t * k]) % m

        return dp[-1]
