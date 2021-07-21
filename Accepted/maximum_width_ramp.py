"""
https://leetcode.com/problems/maximum-width-ramp/
"""


class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        """
        1. Maintain a decreasing stack by scanning nums from left to right.
        2. Then scan the nums from right to left and calculate the maxWidth
            between each ramp.
        """
        maxWidth = 0
        descStack = []

        # Generate decreasing stack.
        for i, num in enumerate(nums):
            if not descStack or nums[descStack[-1]] > num:
                descStack.append(i)

        # Check elements from right to left.
        for j in reversed(range(len(nums))):
            while descStack and nums[descStack[-1]] <= nums[j]:
                maxWidth = max(maxWidth, j - descStack.pop())

        return maxWidth
