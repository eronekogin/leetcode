"""
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
"""


class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        """
        Suppose dp[i, j] stands for the longest subsequence ending at (i, j),
        then dp[i, j] = dp[j - i, i] + 1 or 2 if j - i does not exist.
        """
        dp = {}
        memo = set(arr)
        N = len(arr)
        for j in range(N):
            for i in range(j):
                a, b = arr[i], arr[j]
                if b - a < a and b - a in memo:
                    dp[(a, b)] = dp.get((b - a, a), 2) + 1

        return max(dp.values() or [0])


print(Solution().lenLongestFibSubseq(
    [1, 2, 3, 4, 5, 6, 7, 8]))
