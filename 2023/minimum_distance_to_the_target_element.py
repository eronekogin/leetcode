"""
https://leetcode.com/problems/minimum-distance-to-the-target-element/
"""


class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        minDistance = len(nums) + 1
        for i, num in enumerate(nums):
            if num == target:
                minDistance = min(minDistance, abs(i - start))

        return minDistance
