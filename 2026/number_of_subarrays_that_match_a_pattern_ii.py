"""
https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/description/
"""


from itertools import pairwise


class Solution:
    """
    Solution
    """

    def count_matching_subarrays(self, nums: list[int], pattern: list[int]) -> int:
        """
        count matching subarrays
        """
        def kmp(s: list[int]):
            n = len(s)
            dp = [0] * n
            for i in range(1, n):
                v = dp[i - 1]
                while v and s[v] != s[i]:
                    v = dp[v - 1]

                dp[i] = v + (s[i] == s[v])

            return dp

        diffs = [(b > a) - (a > b) for a, b in pairwise(nums)]
        dp = kmp(pattern + [215] + diffs)
        return dp.count(len(pattern))
