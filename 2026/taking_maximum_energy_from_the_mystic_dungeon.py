"""
https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_energy(self, energy: list[int], k: int) -> int:
        """
        Each end point's sum comes from the previous sum + energy[end],
        for every end point <= len(energy) - k - 1
        """
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]

        return max(energy)
