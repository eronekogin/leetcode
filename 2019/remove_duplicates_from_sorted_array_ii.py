"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        MAX_DUP_ALLOWED = 2
        i = 0
        for num in nums:
            if i < MAX_DUP_ALLOWED or num > nums[i - MAX_DUP_ALLOWED]:
                nums[i] = num
                i += 1

        return i


nums = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(nums))
