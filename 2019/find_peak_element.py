"""
https://leetcode.com/problems/find-peak-element/
"""


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None

        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + ((high - low) >> 1)  # = (low + high) // 2
            if nums[mid] < nums[mid + 1]:  # Ascending.
                low = mid + 1
            elif nums[mid] > nums[mid + 1]:  # Descending.
                high = mid

        return low


nums = [1, 2, 1, 3, 5, 6, 4]
print(Solution().findPeakElement(nums))
