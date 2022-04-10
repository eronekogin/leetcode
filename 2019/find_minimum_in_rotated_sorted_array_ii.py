"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Use binary search solution. Preassumption: the input nums is not empty.
        """
        n = len(nums) - 1
        if not n:  # nums only contains 1 number.
            return nums[0]

        if nums[-1] > nums[0]:  # The whole list is already in ascending order.
            return nums[0]

        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:  # nums[mid] == nums[right]
                if nums[left] == nums[right]:  # Get rid of duplicates.
                    left += 1
                    right -= 1
                else:
                    right = mid

        return nums[right]


nums = [1, 2, 3]
print(Solution().findMin(nums))
