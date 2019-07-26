"""
https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeftHeight, maxRightHeight = 0, 0
        rslt = 0

        while l < r:
            if height[l] < height[r]:
                # For the index l, found a taller bar on its right side.
                if height[l] < maxLeftHeight:
                    # If the current bar is less than the max left height,
                    # It at least can hold the below water.
                    rslt += maxLeftHeight - height[l]
                else:
                    # If the current bar is greater or equal than the max
                    # left height, it becomes the new max left height.
                    maxLeftHeight = height[l]

                l += 1  # Processing next l.
            else:
                # For the index r, found a taller bar on its left side.
                if height[r] < maxRightHeight:
                    # If the current bar is less than the max right height,
                    # it at least can hold the below water.
                    rslt += maxRightHeight - height[r]
                else:
                    # If the current bar is greater or equal than the max
                    # right height, it becomes the new max right height.
                    maxRightHeight = height[r]

                r -= 1  # Processing next r.

        return rslt


height = [4, 2, 3]
print(Solution().trap(height))
