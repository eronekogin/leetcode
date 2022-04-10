"""
https://leetcode.com/problems/binary-subarrays-with-sum/
"""


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        minStart = maxStart = 0
        minSum = maxSum = 0
        rslt = 0

        for end, x in enumerate(nums):
            minSum += x
            while minStart < end and minSum > goal:
                minSum -= nums[minStart]
                minStart += 1

            maxSum += x
            while maxStart < end and (maxSum > goal or maxSum == goal and not nums[maxStart]):
                maxSum -= nums[maxStart]
                maxStart += 1

            if minSum == goal:
                rslt += maxStart - minStart + 1

        return rslt


print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))
