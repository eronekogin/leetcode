"""
https://leetcode.com/problems/largest-divisible-subset/
"""


from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        1. Sort the input nums first.
        2. Suppose dp[i] is the largest divisible subset with nums[i] as its
            largest element, then we have:
            dp[i + 1] = dp[k] + [nums[i + 1]], where:
            a. j in [0, i].
            b. nums[i + 1] % nums[j] == 0.
            c. dp[k] has the max length among the above dp[j]s.
        """
        if not nums:
            return []

        maxLen = len(nums)
        sortedNums = sorted(nums)
        dp = [[] for _ in range(maxLen)]
        dp[0].append(nums[0])
        maxList = []
        for i in range(1, maxLen):
            largestSubList = []
            for j in reversed(range(i)):
                if sortedNums[i] % sortedNums[j] == 0 and len(
                        dp[j]) > len(largestSubList):
                    largestSubList = dp[j]

            dp[i] = largestSubList + [sortedNums[i]]
            if len(dp[i]) > len(maxList):
                maxList = dp[i]

        return maxList


print(Solution().largestDivisibleSubset([1, 2, 4, 8]))
