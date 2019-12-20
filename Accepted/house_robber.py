"""
https://leetcode.com/problems/house-robber/
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        preMax = currMax = 0
        for num in nums:
            # The max robbed money for the next house could be:
            # 1. Rob the next house: preMax + num
            # 2. Don't rob the next house: currMax
            preMax, currMax = currMax, max(preMax + num, currMax)

        return currMax


print(Solution().rob([1, 2, 3, 1]))
