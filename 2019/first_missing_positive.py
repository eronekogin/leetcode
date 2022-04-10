"""
https://leetcode.com/problems/first-missing-positive/
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # By given a list of numbers with length k, the first missing
        # positive number will fall in [1, k + 1]. So add one element 0
        # to the given nums to make its total length to be k + 1.
        nums.append(0)
        totalLen = len(nums)

        # Pass 1: Clear the invalid numbers in nums.
        for i, n in enumerate(nums):
            if n < 0 or n >= totalLen:
                nums[i] = 0

        # Pass 2: Calculate frequency of each i in nums.
        for i, n in enumerate(nums):
            nums[n % totalLen] += totalLen

        # Pass 3: For a nums[i], if its value is less than totalLen,
        # it means it never occurred in the array.
        for i in range(1, totalLen):  # Skip index 0.
            if nums[i] < totalLen:
                return i

        # When coming here, it means all the 1 to k are found in the list
        # and k + 1 is missing.
        return totalLen


nums = [3, 4, -1, 1]
print(Solution().firstMissingPositive(nums))
