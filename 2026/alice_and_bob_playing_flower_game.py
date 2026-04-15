"""
https://leetcode.com/problems/alice-and-bob-playing-flower-game/description/
"""


class Solution:
    """
    Solution
    """

    def flower_game(self, n: int, m: int) -> int:
        """
        The winning condition is there should be no flower left on both lanes.

        So x + y must be odd for Alice to win the game since she is the first picker:

        * x is odd, y is even -> ceil(n / 2) * floor(m / 2)
        * x is even, y is odd -> floor(n / 2) * ceil(m / 2)

        So total = ceil(n / 2) * floor(m / 2) + floor(n / 2) * ceil(m / 2)

        if n and m are even: total = nm / 2
        if n and m are odd: total = (nm - 1) / 2
        otherwise: total = nm / 2

        So the result is floor(nm / 2)
        """
        return (n * m) >> 1
