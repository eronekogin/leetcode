"""
https://leetcode.com/problems/patching-array/
"""


from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        Suppose miss is the smallest summary in range [0, n] that we might be
        missing, which means we already know we can build all sums in [0, miss).
        Then:
        1. If the next number in the given list is less than miss, we can add
        it to the above sum range to extend it to [0, miss + num).
        2. If the next number in the given list is greater than miss, we must
        add a new number into the list in order to complete the range. For
        minimum add times, it's best we just add the miss itself to reach the
        largest range.
        """
        currMiss, needToAdd, i, maxLen = 1, 0, 0, len(nums)
        while currMiss <= n:  # Still has missing summary.
            if i < maxLen and nums[i] <= currMiss:  # Case 1.
                currMiss += nums[i]  # Add the current number in the list.
                i += 1
            else:  # Case 2.
                currMiss += currMiss  # Add itself.
                needToAdd += 1

        return needToAdd
