"""
https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        mostWater = 0
        total = len(height)

        for i in range(total):
            for j in range(i + 1, total):
                currWater = min(height[i], height[j]) * (j - i)
                mostWater = max(currWater, mostWater)

        return mostWater
