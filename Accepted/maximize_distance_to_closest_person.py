"""
https://leetcode.com/problems/maximize-distance-to-closest-person/
"""


from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start = maxInterval = 0
        for end in range(1, len(seats)):
            if seats[end]:
                if seats[start]:
                    maxInterval = max(maxInterval, (end - start) >> 1)
                else:
                    maxInterval = max(maxInterval, end - start)

                start = end

        return max(maxInterval, len(seats) - 1 - start)
