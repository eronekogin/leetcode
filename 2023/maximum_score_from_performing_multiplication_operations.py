"""
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
"""


class Solution:
    def maximumScore(self, nums: list[int], multipliers: list[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for currLeft in range(m - 1, -1, -1):
            for totalPicked in range(m - 1, -1, -1):
                currRight = n - 1 - (totalPicked - currLeft)
                if currRight < 0 or currRight >= n:
                    break

                leftPicked = (
                    dp[currLeft + 1][totalPicked + 1] +
                    nums[currLeft] * multipliers[totalPicked]
                )
                rightPicked = (
                    dp[currLeft][totalPicked + 1] +
                    nums[currRight] * multipliers[totalPicked]
                )
                dp[currLeft][totalPicked] = max(leftPicked, rightPicked)

        return dp[0][0]


print(Solution().maximumScore([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]))
