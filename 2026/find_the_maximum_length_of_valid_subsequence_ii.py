"""
https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_length(self, nums: list[int], k: int) -> int:
        """
        maximum length
        """
        rslt = 0
        for r in range(k):
            dp = [0] * k
            for x in nums:
                dp[x % k] = dp[r - (x % k)] + 1

            rslt = max(dp + [rslt])

        return rslt


print(Solution().maximum_length([1, 4, 2, 3, 1, 4], 3))
