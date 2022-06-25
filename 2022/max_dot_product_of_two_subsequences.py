"""
https://leetcode.com/problems/max-dot-product-of-two-subsequences/
"""


class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Suppose dp[i][j] is the maximum dot product when the subsequence 1 is
        ending at index i in nums1 and the subsequence 2 is ending at index j
        in nums2.
        """
        R, C = len(nums1), len(nums2)
        dp = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                dp[r][c] = nums1[r] * nums2[c]
                if r > 0 and c > 0:
                    dp[r][c] += max(dp[r - 1][c - 1], 0)

                if r > 0:
                    dp[r][c] = max(dp[r][c], dp[r - 1][c])

                if c > 0:
                    dp[r][c] = max(dp[r][c], dp[r][c - 1])

        return dp[-1][-1]
