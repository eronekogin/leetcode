"""
https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: 'List[int]', val: int) -> int:
        total, i = len(nums), 0

        while i < total:
            if nums[i] == val:  # Found a target.
                nums[i] = nums[total - 1]  # Swap it with the last element.
                # Reduce total so that the last element is disposed from
                # the current array.
                total -= 1
            else:
                i += 1  # Advance i.
        
        return total  # Now total stores the final valid length.

