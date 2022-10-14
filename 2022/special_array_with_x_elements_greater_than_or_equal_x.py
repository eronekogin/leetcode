"""
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
"""


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        sortedNums = sorted(nums, reverse=True)
        N = len(nums)
        for i in range(N):
            x = i + 1
            if sortedNums[i] >= x:  # Now we have x numbers >= x.
                if i == len(nums) - 1 or sortedNums[i + 1] < x:
                    # Make sure exactly x numbers are >= x:
                    # 1. No more numbers left.
                    # 2. The next number is less than x.
                    return x

        return -1
