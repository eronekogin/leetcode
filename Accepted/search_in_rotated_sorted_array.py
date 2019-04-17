"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)

        while low < high:
            middle = (low + high) // 2
            if target < nums[0] < nums[middle]:  # -inf.
                low = middle + 1
            elif target >= nums[0] > nums[middle]:  # +inf.
                high = middle
            elif target > nums[middle]:
                low = middle + 1
            elif target < nums[middle]:
                high = middle
            else:  # target == nums[middle]
                return middle

        return -1  # Not found.


print(Solution().search([1, 3], 1))
