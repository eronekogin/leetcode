"""
https://leetcode.com/problems/find-pivot-index/
"""


from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for i, num in enumerate(nums):
            if left + num == right:
                return i

            left += num
            right -= num

        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
