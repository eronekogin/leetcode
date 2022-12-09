"""
https://leetcode.com/problems/stone-game-vii/
"""


class Solution:
    def stoneGameVII(self, stones: list[int]) -> int:
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + stones[i]

        def getSum(left, right):
            return preSum[right + 1] - preSum[left]

        dp = [[0] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                scoreRemoveLeftMost = getSum(l + 1, r)
                scoreRemoveRightMost = getSum(l, r - 1)
                dp[l][r] = max(scoreRemoveLeftMost - dp[l + 1][r],
                               scoreRemoveRightMost - dp[l][r - 1])
        return dp[0][n - 1]


print(Solution().stoneGameVII([5, 3, 1, 4, 2]))
