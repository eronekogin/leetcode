"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
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
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


nums = [1, 2, 3]
print(Solution().findMin(nums))
