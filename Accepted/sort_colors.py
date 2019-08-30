"""
https://leetcode.com/problems/sort-colors/
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # One pass solution using three pointers.
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:  # Case red.
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:  # Case white.
                white += 1
            else:  # Case blue.
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


nums = [2, 0, 2, 1, 1, 0]
print(Solution().sortColors(nums))
