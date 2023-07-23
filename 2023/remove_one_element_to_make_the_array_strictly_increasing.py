"""
https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
"""


class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        """
        when nums[i - 1] >= nums[i]:

            1. If nums[i - 2] >= nums[i], we should remove the ith number.
            2. Else, we should remove the i - 1 th number.
        """
        removes = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                removes += 1
                if removes > 1:
                    return False
                
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
        
        return removes < 2
