"""
https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_ways(self, corridor: str) -> int:
        """
        number of ways
        """
        seat_indexes = [i for i, c in enumerate(corridor) if c == 'S']
        if len(seat_indexes) < 2 or len(seat_indexes) & 1:
            return 0

        ways = 1
        for i in range(1, len(seat_indexes) - 1, 2):
            # There are s[i + 1] - s[i] number of ways to
            # install a divider between two adjancent seats
            ways *= seat_indexes[i + 1] - seat_indexes[i]

        return ways % (10 ** 9 + 7)
