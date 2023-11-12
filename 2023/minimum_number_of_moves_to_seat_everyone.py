"""
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
"""


class Solution:
    """
    Solution
    """

    def min_moves_to_seat(self, seats: list[int], students: list[int]) -> int:
        """
        min_moves_to_seat
        """
        return sum(abs(b - a) for a, b in zip(sorted(seats), sorted(students)))
