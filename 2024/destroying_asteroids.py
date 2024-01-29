"""
https://leetcode.com/problems/destroying-asteroids/description/
"""


class Solution:
    """
    Solution
    """

    def asteroids_destroyed(self, mass: int, asteroids: list[int]) -> bool:
        """
        asteroids_destroyed
        """
        sorted_asteroids = sorted(asteroids)
        max_mass = sorted_asteroids[-1]
        curr_mass = mass
        for m in sorted_asteroids:
            if curr_mass < m:
                return False

            curr_mass += m
            if curr_mass >= max_mass:
                return True

        return False
