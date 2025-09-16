"""
https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_jumps(self, nums: list[int], target: int) -> int:
        """
        maximum jumps
        """
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for end in range(1, n):
            for start in range(end - 1, -1, -1):
                if abs(nums[end] - nums[start]) <= target:
                    if dp[start] > -1:
                        dp[end] = max(dp[end], dp[start] + 1)

        return dp[-1]


print(Solution().maximum_jumps([1, 3, 6, 4, 1, 2], 2))
