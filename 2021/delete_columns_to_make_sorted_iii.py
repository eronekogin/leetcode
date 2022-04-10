"""
https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
"""


class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """
        1. Take n cols as n elements, so we have an array of n elements:
            => The final array has every row in lexicographic order.
            => The elements in final state is in increasing order.
            => The final elements is a sub sequence of initial array.
            => Transform the problem to find the maximum increasing
                subsequence.
        2. Suppose dp[i] is the longest subsequence ends with i-th element,
            then we have:
            for all i < j, dp[j] = max(dp[j], dp[i] + 1)
        """
        N = len(strs[0])
        dp = [1] * N
        for j in range(1, N):
            for i in range(j):
                if all(w[i] <= w[j] for w in strs):
                    dp[j] = max(dp[j], dp[i] + 1)

        return N - max(dp)
