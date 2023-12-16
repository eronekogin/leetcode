"""
https://leetcode.com/problems/watering-plants/
"""


class Solution:
    """
    Solution
    """

    def watering_plants(self, plants: list[int], capacity: int) -> int:
        """
        watering_plants
        """
        steps = 0
        curr_water = capacity
        n = len(plants)
        for i, need_water in enumerate(plants):
            steps += 1
            curr_water -= need_water

            # check next plant.
            if i + 1 < n and curr_water < plants[i + 1]:
                steps += (i + 1) << 1  # Need to get back to river and refill.
                curr_water = capacity

        return steps
