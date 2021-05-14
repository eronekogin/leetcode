"""
https://leetcode.com/problems/minimum-number-of-refueling-stops/
"""


from heapq import heappop, heappush


class Solution:
    def minRefuelStops(
            self,
            target: int,
            startFuel: int,
            stations: list[list[int]]) -> int:
        """
        Keep driving until no fuel left. Then take the maximum refuel from
        the previous gas station. If we cannot reach to the current location,
        the task is impossible.
        """
        heap = []
        refuledStops = prevLocation = 0
        tank = startFuel
        for currlocation, capacity in stations + [(target, float('inf'))]:
            tank -= currlocation - prevLocation
            while heap and tank < 0:  # Must refuel now.
                tank += -heappop(heap)
                refuledStops += 1

            if tank < 0:
                # Don't have enough fuel to reach the current location.
                return -1

            heappush(heap, -capacity)
            prevLocation = currlocation

        return refuledStops
