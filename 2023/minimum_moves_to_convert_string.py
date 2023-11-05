"""
https://leetcode.com/problems/minimum-moves-to-convert-string/
"""


class Solution:
    """
    Solution
    """

    def minimum_moves(self, s: str) -> int:
        """
        minimum_moves
        """
        i, n, actions = 0, len(s), 0
        while i < n:
            if s[i] == 'X':
                actions += 1
                i += 3
            else:
                i += 1

        return actions
