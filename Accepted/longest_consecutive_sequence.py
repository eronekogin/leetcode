"""
https://leetcode.com/problems/longest-consecutive-sequence/
"""


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen, numSet = 0, set(nums)
        for num in numSet:
            if num - 1 not in numSet:
                # num is the minimum number in its consecutive sequence.
                maxNum = num + 1
                while maxNum in numSet:
                    # found higher number in its consecutive sequence.
                    maxNum += 1

                maxLen = max(maxLen, maxNum - num)

        return maxLen
