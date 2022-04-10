"""
https://leetcode.com/problems/car-fleet/
"""


class Solution:
    def carFleet(
            self, target: int, position: list[int], speed: list[int]) -> int:
        """
        1. If the car at the furthest position could reach the target faster
            than any other cars behind it, it will form a fleet itself.
        2. If the cars after the leading car could reach the target earlier
            than the leading car, it will form a fleet with the leading car.
        """
        fleets = 0
        timeCosts = [
            (target - p) / s for p, s in sorted(zip(position, speed))]
        while len(timeCosts) > 1:
            lead = timeCosts.pop()
            if lead < timeCosts[-1]:
                fleets += 1
            else:
                timeCosts[-1] = lead

        return fleets + len(timeCosts)  # Add last car if any.


target = 10
position = [8, 3, 7, 4, 6, 5]
speed = [4, 4, 4, 4, 4, 4]
print(Solution().carFleet(target, position, speed))
