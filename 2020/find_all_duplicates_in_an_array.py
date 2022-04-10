"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        rslt = []
        for num in nums:
            if nums[abs(num) - 1] < 0:  # Visited before.
                rslt.append(abs(num))
            else:  # First visit, mark the current number negative.
                nums[abs(num) - 1] *= -1

        return rslt


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
