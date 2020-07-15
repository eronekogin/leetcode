"""
https://leetcode.com/problems/heaters/
"""


from typing import List
from bisect import bisect_left


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        r, n = 0, len(heaters)
        for h in houses:
            # Try to find which heater pairs the current house is between.
            i = bisect_left(heaters, h)
            if i == 0:  # On the left side of the first heater.
                r = max(r, heaters[0] - h)
            elif i == n:  # On the right side of the last heater.
                r = max(r, h - heaters[-1])
            else:  # Between two heaters, try to find the mininum distance.
                r = max(r, min(h - heaters[i - 1], heaters[i] - h))

        return r
