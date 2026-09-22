"""
https://leetcode.com/problems/find-the-winning-player-in-coin-game/description/
"""


class Solution:
    """
    Solution
    """

    def winning_player(self, x: int, y: int) -> str:
        """
        winning player
        """
        is_alice = False

        while x >= 1 and y >= 4:
            is_alice = not is_alice
            x -= 1
            y -= 4

        if is_alice:
            return 'Alice'

        return 'Bob'
