"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        rslt = [-1, -1]
        if not nums:  # Empty list.
            return rslt

        low, high = 0, len(nums) - 1
        while low < high:  # Find the lower bound first.
            mid = (low + high) >> 1  # Calulate mid aligned with left.
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        if nums[low] != target:  # Target not found.
            return rslt

        rslt[0] = low  # Found the low boudary.
        high = len(nums) - 1
        while low < high:  # Then find the higher bound.
            mid = ((low + high) >> 1) + 1  # Calculate mid aligned with right.
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid

        # Don't need to check if the element equals to the target again.
        rslt[1] = high  # Found the higher boundary.
        return rslt


nums, t = [5, 7, 7, 8, 8, 10], 7
print(Solution().searchRange(nums, t))
