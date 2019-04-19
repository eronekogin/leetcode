"""
https://leetcode.com/problems/search-insert-position/
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None:
            return 0

        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low


print(Solution().searchInsert([1, 3, 5, 6], 0))
