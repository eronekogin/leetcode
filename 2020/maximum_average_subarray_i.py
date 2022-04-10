"""
https://leetcode.com/problems/maximum-average-subarray-i/
"""


from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        maxSum = currSum = sum(nums[:k])
        for end in range(k, len(nums)):
            currSum += nums[end] - nums[start]
            start += 1
            maxSum = max(maxSum, currSum)

        return maxSum / k


print(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4))
