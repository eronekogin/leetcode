"""
https://leetcode.com/problems/jump-game-vi/
"""


from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        N = len(nums)
        dp = [0] * N  # dp[i] stands for maximum score starting from index i.
        dp[0] = nums[0]
        q = deque([0])
        for i in range(1, N):
            # Cannot reach currend index from top of the queue.
            if q[0] < i - k:
                q.popleft()

            dp[i] = nums[i] + dp[q[0]]
            # The tail items will never be picked later..
            while q and dp[q[-1]] <= dp[i]:
                q.pop()

            q.append(i)

        return dp[-1]
