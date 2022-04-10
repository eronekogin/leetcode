"""
https://leetcode.com/problems/squares-of-a-sorted-array/
"""


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return [x ** 2 for x in nums]

        if nums[-1] < 0:
            return [x ** 2 for x in reversed(nums)]

        n = len(nums)
        left, right = 0, n - 1
        rslt = [None] * n
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                rslt[i] = nums[right] ** 2
                right -= 1
            else:
                rslt[i] = nums[left] ** 2
                left += 1

        return rslt


print(Solution().sortedSquares([-2, -1, 3]))
