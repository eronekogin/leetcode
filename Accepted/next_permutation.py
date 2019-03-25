"""
https://leetcode.com/problems/next-permutation/
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        totalLen = len(nums)
        i = totalLen - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # Found an exchange position.
            j = totalLen - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]  # Exchange i, j.

        # Then reverse the part of list starting from i + 1.
        l, r = i + 1, totalLen - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return


nums = [2, 3, 1]
Solution().nextPermutation(nums)
print(nums)
