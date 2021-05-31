"""
https://leetcode.com/problems/monotonic-array/
"""


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        isIncreasing = isDecreasing = True
        for x, y in zip(nums, nums[1:]):
            if y > x:
                isDecreasing = False
            elif x > y:
                isIncreasing = False

        return isIncreasing or isDecreasing


print(Solution().isMonotonic([1, 2, 2, 3]))
