"""
https://leetcode.com/problems/total-distance-traveled/description/
"""


class Solution:
    """
    Solution
    """

    def distance_traveled(self, main_tank: int, additional_tank: int) -> int:
        """
        distance traveled
        """
        distance = 0
        while main_tank >= 5:
            distance += 50
            main_tank -= 5
            if additional_tank > 0:
                main_tank += 1
                additional_tank -= 1

        return distance + main_tank * 10
