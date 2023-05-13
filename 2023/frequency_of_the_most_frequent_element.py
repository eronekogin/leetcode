"""
https://leetcode.com/problems/frequency-of-the-most-frequent-element/
"""


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        """
        1. Sort the nums in ascending order.

        2. For the sliding window from [start, end], add nums[end] to the
            current sum, then check if the current sum is >= 
            nums[end] * (end - start + 1), which means if it is possible to
            make all numbers inside this window the same.

        3. When reaching the end, return the current size of the sliding
            window. 
        """
        start = 0
        sortedNums = sorted(nums)
        currSum = k
        for end in range(len(sortedNums)):
            currSum += sortedNums[end]
            if currSum < sortedNums[end] * (end - start + 1):
                currSum -= sortedNums[start]
                start += 1

        return end - start + 1
