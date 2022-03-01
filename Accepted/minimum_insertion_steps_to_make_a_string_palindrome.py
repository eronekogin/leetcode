"""
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        """
        Find the longest palindrome subsequence in s first, then the required
        insertion steps is N - len(subSequence).
        """
        def check(start: int, end: int) -> int:
            if not memo[start][end]:
                if start > end:
                    return 0

                if start == end:
                    return 1

                if s[start] == s[end]:
                    memo[start][end] = check(start + 1, end - 1) + 2
                else:
                    memo[start][end] = max(
                        check(start + 1, end),
                        check(start, end - 1)
                    )

            return memo[start][end]

        N = len(s)
        memo = [[0] * N for _ in range(N)]
        return N - check(0, N - 1)
