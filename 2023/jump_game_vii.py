"""
https://leetcode.com/problems/jump-game-vii/
"""


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # dp[i] stands for if position i is reachable.
        dp = [c == '0' for c in s]

        # Number of previous positions that can reach the current position.
        prev = 0

        for i in range(1, len(s)):
            if i >= minJump:
                prev += dp[i - minJump]

            if i > maxJump:
                prev -= dp[i - maxJump - 1]

            dp[i] &= prev > 0

        return dp[-1]
