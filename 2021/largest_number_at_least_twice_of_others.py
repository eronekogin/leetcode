"""
https://leetcode.com/problems/largest-number-at-least-twice-of-others/
"""


from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxIdx, secondMaxIdx = 0, None
        for i in range(1, len(nums)):
            if nums[i] > nums[maxIdx]:
                maxIdx, secondMaxIdx = i, maxIdx
            elif secondMaxIdx is None:
                secondMaxIdx = i
            elif nums[i] > nums[secondMaxIdx]:
                secondMaxIdx = i

        if secondMaxIdx is not None and nums[maxIdx] < nums[secondMaxIdx] << 1:
            maxIdx = -1

        return maxIdx


print(Solution().dominantIndex([3, 6, 1, 0]))
