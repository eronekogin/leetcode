"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        pivots: list[int] = []
        for i, num in enumerate(nums):
            if num == 0:
                pivots.append(i)

        # Contains no zero or one zero, must delete 1 number.
        if len(pivots) < 2:
            return len(nums) - 1

        # Add front and end.
        pivots = [-1] + pivots + [len(nums)]

        # Calculate maximum length.
        maxSize = 0
        for i in range(1, len(pivots) - 1):
            maxSize = max(
                maxSize,
                max(0, pivots[i] - pivots[i - 1] - 1) +
                max(0, pivots[i + 1] - pivots[i] - 1)
            )

        return maxSize


print(Solution().longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1]))
