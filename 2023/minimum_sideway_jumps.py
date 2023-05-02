"""
https://leetcode.com/problems/minimum-sideway-jumps/
"""


class Solution:
    def minSideJumps(self, obstacles: list[int]) -> int:
        """
        Suppose dp[i] stands for the minimum jumps needed to reach the target
        lane i + 1, and when we find a stone on the current lane, we make
        dp[i] large enough so that it can not be achievable.
        """
        dp = [1, 0, 1]
        for x in obstacles:
            if x:
                dp[x - 1] = len(obstacles) + 1

            for i in range(3):
                if x != i + 1:
                    dp[i] = min(
                        dp[i],
                        dp[(i + 1) % 3] + 1,
                        dp[(i + 2) % 3] + 1
                    )

        return min(dp)


print(Solution().minSideJumps([0, 1, 2, 3, 0]))
