"""
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
"""


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        """
        1. Suppose dp[s][p] stands the number of ways to walk exactly s steps
            starting from position p back to index 0, then we have:
            dp[s][p] = dp[s - 1][p - 1] + dp[s - 1][p + 1] + dp[s - 1][p].
        2. Then we could further reduce it to 1D array.
        """
        # Can only walk maximum half of steps right from index 0 as we need to
        # come back later.
        maxPos = min(1 + (steps >> 1), arrLen)
        currDp = [0] * (maxPos + 1)
        currDp[0] = 1
        for _ in range(steps):
            nextDp = [0] * (maxPos + 1)
            for i in range(maxPos):
                nextDp[i] = currDp[i] + currDp[i + 1]
                if i:
                    nextDp[i] += currDp[i - 1]

            currDp = nextDp

        return currDp[0] % (10 ** 9 + 7)
