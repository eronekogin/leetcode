"""
https://leetcode.com/problems/count-different-palindromic-subsequences/
"""


class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        """
        Suppose dp[i][j] is the answer for S[i: j + 1], then we have:

            1. dp[i][j] contains all the unique single char inside S[i: j + 1].

            2. Then since the elements in S could only be a, b, c, d, the
                remaining non-empty palindrome must be a_a, b_b, c_c or d_d,
                where _ stands for 0 or more chars.

            3. So for each char in 'abcd', we check if any pairs occurs inside
                S[i: j + 1], if so, add the rslt to the dp[i][j].
        """
        def count(start: int, end: int) -> int:
            if dp[start][end] is None:
                cnt = 1  # Count for empty string.
                if start <= end:
                    for x in range(4):  # Check for a, b, c, d.
                        l, r = nexts[start][x], prevs[end][x]
                        if l is not None:
                            if start <= l <= end:
                                cnt += 1  # left x is inside S[start: end + 1].

                            if r is not None and l < r:
                                # right x is inside S[start: end + 1].
                                cnt += count(l + 1, r - 1)  # Counting x_x.

                cnt %= MOD
                dp[start][end] = cnt

            return dp[start][end]

        N, OFFSET, MOD = len(S), ord('a'), 10 ** 9 + 7
        A = [ord(c) - OFFSET for c in S]

        # Calculate the previous list which contains indexes of the nearest a,
        # b, c, d <= the current index i.
        currIndexes, prevs = [None] * 4, [None] * N
        for i in range(N):
            currIndexes[A[i]] = i
            prevs[i] = tuple(currIndexes)

        # Calculate the next list which contains indexes of the nearest a, b,
        # c, d >= the current index i.
        currIndexes, nexts = [None] * 4, [None] * N
        for i in range(N - 1, -1, -1):
            currIndexes[A[i]] = i
            nexts[i] = tuple(currIndexes)

        dp = [[None] * N for _ in range(N)]
        return count(0, N - 1) - 1  # Remove the outter most empty string.
