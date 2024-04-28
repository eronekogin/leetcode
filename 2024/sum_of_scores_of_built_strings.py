"""
https://leetcode.com/problems/sum-of-scores-of-built-strings/description/
"""


class Solution:
    """
    Solution
    """

    def sum_scores(self, s: str) -> int:
        """
        memo[i] stands for the longest common prefix starting at index i
        comparing to the one starting at the index 0.
        """
        n = len(s)
        memo = [0] * n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                memo[i] = min(r - i + 1, memo[i - l])

            while i + memo[i] < n and s[memo[i]] == s[i + memo[i]]:
                memo[i] += 1

            if i + memo[i] - 1 > r:
                l, r = i, i + memo[i] - 1

        return sum(memo) + n  # add last suffix which starts at index 0.
