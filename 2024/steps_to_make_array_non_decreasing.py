"""
https://leetcode.com/problems/steps-to-make-array-non-decreasing/description/
"""


class Solution:
    """
    Solution
    """

    def total_steps(self, nums: list[int]) -> int:
        """
        total steps
        """
        n = len(nums)
        dp = [0] * n
        stack: list[int] = []

        for i in range(n - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])

            stack.append(i)

        return max(dp)


print(Solution().total_steps([5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]))
