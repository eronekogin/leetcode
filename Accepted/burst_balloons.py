"""
https://leetcode.com/problems/burst-balloons/
"""


from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Use dynamic planning.
        Suppose dp[i][j] is the maximum coins we could get between
        ballon i and j (exclusive), and if the kth ballon between i and j 
        is the last ballon to burst, then we could have:

        dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])

        for k in [i + 1, j - 1].

        The reason is that if the kth ballon is the last one to burst, then
        there will only be ballon i, ballon k, ballon j, so the final coin
        will be nums[i] * nums[k] * nums[j]. And we also need to sum the coins
        collected from i to k and from k to j. Since any ballon between i and j
        could be the last one to burst, we need to find out the maximum value
        from that list.
        """
        # First burst any ballons that have zero value.
        # Notice that nums[-1] and nums[n] should also be 1.
        ballons = [1] + [i for i in nums if i] + [1]
        n = len(ballons)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                dp[i][j] = max([
                    dp[i][k] + dp[k][j] +
                    ballons[i] * ballons[k] * ballons[j]
                    for k in range(i + 1, j)
                ])

        return dp[0][n - 1]


print(Solution().maxCoins([3, 1, 5, 8]))
