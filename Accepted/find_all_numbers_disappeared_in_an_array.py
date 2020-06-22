"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            chkIdx = abs(num) - 1
            if nums[chkIdx] > 0:  # Not visited before.
                nums[chkIdx] *= -1

        return [i + 1 for i, num in enumerate(nums) if num > 0]


print(Solution().findDisappearedNumbers([1, 1]))
