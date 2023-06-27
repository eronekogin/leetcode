"""
https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/
"""


class Solution:
    def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        """
        dp[j] / speed stands for the minimum arrival time after j skips.
        """
        N = len(dist)
        dp: list[float] = [0] * (N + 1)
        for i, d in enumerate(dist):
            for j in range(N, -1, -1):
                dp[j] += d
                if i < N - 1:
                    dp[j] = (dp[j] + speed - 1) // speed * speed
                
                if j:
                    dp[j] = min(dp[j], dp[j - 1] + d)
        
        target = speed * hoursBefore
        for i, t in enumerate(dp):
            if t <= target:
                return i
        
        return -1

