"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""


from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        The question could be transformed to find the longest sub list whose
        summary is sum(nums) - x.
        """
        targetSum = sum(nums) - x
        if targetSum < 0:  # Not found.
            return -1

        if targetSum == 0:  # Delete all items.
            return len(nums)

        start, currSum, N = 0, nums[0], len(nums)
        maxLen = -1
        for end in range(1, N):
            currSum += nums[end]
            while start < N and currSum > targetSum:
                currSum -= nums[start]
                start += 1

            if currSum == targetSum:
                maxLen = max(maxLen, end - start + 1)

        if maxLen < 0:  # Not found.
            return -1

        return N - maxLen


print(Solution().minOperations(
    [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000,
     10000, 9999, 9993, 9904, 8819, 1231, 6309], 134365))
