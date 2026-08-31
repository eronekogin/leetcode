"""
https://leetcode.com/problems/maximum-points-after-enemy-battles/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_points(self, enemy_energies: list[int], current_energy: int) -> int:
        """
        maximum points
        """
        min_energy = min(enemy_energies)
        total_energy = sum(enemy_energies)

        if current_energy < min_energy:
            return 0

        return (current_energy + total_energy - min_energy) // min_energy
