"""
https://leetcode.com/problems/find-the-middle-index-in-array/
"""


from itertools import accumulate


class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        preSums = [0] + list(accumulate(nums))
        check = preSums[0] + preSums[-1]
        for i in range(len(nums)):
            if preSums[i] + preSums[i + 1] == check:
                return i

        return -1  # Not found.


print(Solution().findMiddleIndex([2,3,-1,8,4]))