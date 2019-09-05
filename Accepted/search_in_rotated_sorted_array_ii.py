"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:  # Found.
                return True

            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # nums[m] == nums[r].
                r -= 1  # Remove duplicates until new r is found.

        return False  # Not Found.


nums = [3, 1]
target = 1
print(Solution().search(nums, target))
