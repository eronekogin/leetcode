"""
https://leetcode.com/problems/greatest-sum-divisible-by-three/
"""


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        """
        dp[0] stands for the maximum sum divisible by 3.
        dp[1] stands for the maximum sum divided by 3 with remainder 1.
        dp[2] stands for the maximum sum divided by 3 with remainder 2.
        """
        dp = [0, 0, 0]
        for num in nums:
            for currSum in dp[:]:
                dp[(currSum + num) % 3] = max(
                    dp[(currSum + num) % 3],
                    currSum + num
                )

        return dp[0]


print(Solution().maxSumDivThree([1, 2, 3, 4, 4]))
