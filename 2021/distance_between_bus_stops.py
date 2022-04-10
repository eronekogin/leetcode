"""
https://leetcode.com/problems/distance-between-bus-stops/
"""


class Solution:
    def distanceBetweenBusStops(
        self,
        distance: list[int],
        start: int,
        destination: int
    ) -> int:
        if start == destination:
            return 0

        if start > destination:
            return self.distanceBetweenBusStops(distance, destination, start)

        totalSum = sum(distance)
        currSum = sum(distance[start: destination])
        return min(totalSum - currSum, currSum)
