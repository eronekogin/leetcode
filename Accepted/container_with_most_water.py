"""
https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        l = 0
        r = len(height) - 1
        mostWater = 0

        while l < r:
            """
            Starting at the front and the end of the list, then
            always moving towards elements having higher height
            in order to contain more water.
            """
            mostWater = max(mostWater, min(height[l], height[r]) * (r - l))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return mostWater
