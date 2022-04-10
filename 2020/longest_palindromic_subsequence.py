"""
https://leetcode.com/problems/longest-palindromic-subsequence/
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def check(start: int, end: int) -> int:
            if memo[start][end]:
                return memo[start][end]

            if start > end:
                return 0

            if start == end:
                return 1

            if s[start] == s[end]:
                memo[start][end] = check(start + 1, end - 1) + 2
            else:
                memo[start][end] = max(
                    check(start + 1, end), check(start, end - 1))

            return memo[start][end]

        memo = [[0] * len(s) for _ in range(len(s))]
        return check(0, len(s) - 1)
