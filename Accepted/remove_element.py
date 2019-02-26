"""
https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: 'List[int]', val: int) -> int:
        total = len(nums)
        start = stop = 0

        if total == 0:  # List is empty.
            return 0

        while stop < total:
            while nums[stop] != val and stop < total:
                stop += 1

            start = stop  # Found the first val.
            stop += 1

            while nums[stop] == val and stop < total:  # Skip the dup vals.
                stop += 1

            temp = stop

            while start < temp and stop < total:  # Copy elements.
                nums[start] = nums[stop]
                start += 1
                stop += 1
