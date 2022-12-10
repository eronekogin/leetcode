"""
https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
"""


class Solution:
    def maxHeight(self, cuboids: list[list[int]]) -> int:
        sortedCubs = [[0, 0, 0]] + sorted(map(sorted, cuboids))
        N = len(sortedCubs)
        dp = [0] * N
        for j in range(1, N):
            for i in range(j):
                if all(sortedCubs[i][k] <= sortedCubs[j][k] for k in range(3)):
                    dp[j] = max(dp[j], dp[i] + sortedCubs[j][2])

        return max(dp)
