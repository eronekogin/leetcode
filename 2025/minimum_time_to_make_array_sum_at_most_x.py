"""
https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_time(self, nums1: list[int], nums2: list[int], x: int) -> int:
        """
        minimum time
        """
        n = len(nums1)
        dp = [0] * (n + 1)

        for j, (b, a) in enumerate(sorted(zip(nums2, nums1)), start=1):
            for t in range(j, 0, -1):
                dp[t] = max(dp[t], dp[t - 1] + b * t + a)

        s1, s2 = sum(nums1), sum(nums2)
        for t in range(n + 1):
            if s2 * t + s1 - dp[t] <= x:
                return t

        return -1
