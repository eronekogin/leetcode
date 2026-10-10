"""
https://leetcode.com/problems/snake-in-matrix/description/
"""


class Solution:
    """
    Solution
    """

    def final_position_of_snake(self, n: int, commands: list[str]) -> int:
        """
        final position of snake
        """
        r = c = 0
        for cmd in commands:
            if cmd == 'UP':
                r = max(0, r - 1)
            elif cmd == 'RIGHT':
                c = min(n - 1, c + 1)
            elif cmd == 'DOWN':
                r = min(n - 1, r + 1)
            else:
                c = max(0, c - 1)

        return r * n + c
