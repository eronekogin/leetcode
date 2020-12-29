"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""


from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        Suppose dp[i][j] is the longest common subarray constructed from
        A[i:] and B[j:], then whenever A[i] == B[j],
        dp[i][j] = 1 + dp[i + 1][j + 1]. Then our goal is to find the
        maximum value in dp.
        """
        R, C = len(A), len(B)
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                if A[r] == B[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]

        return max(max(row) for row in dp)


print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
