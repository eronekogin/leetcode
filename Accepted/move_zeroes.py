"""
https://leetcode.com/problems/move-zeroes/
"""


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        zeroStart = 0
        for curr, num in enumerate(nums):
            if num:
                nums[zeroStart], nums[curr] = num, nums[zeroStart]
                zeroStart += 1


print(Solution().moveZeroes([0, 1, 0, 3, 12]))
