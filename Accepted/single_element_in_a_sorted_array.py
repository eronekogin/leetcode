"""
https://leetcode.com/problems/single-element-in-a-sorted-array/
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        The input list is already sorted, so if all the elements
        occur twice, then each pair contains an even index followed
        by an odd index. This pattern will be broken when coming
        across the number that only occurs once.
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + ((r - l) >> 1)

            # If m is odd, m ^ 1 = m - 1
            # if m is even, m ^ 1 = m + 1
            if nums[m] == nums[m ^ 1]:
                # The order of the left half is correct,
                # continue check the right half.
                l = m + 1
            else:
                # The order of the left half is incorrect.
                r = m

        return nums[l]
