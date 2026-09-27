"""
https://leetcode.com/problems/vowels-game-in-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def does_alice_win(self, s: str) -> bool:
        """
        does alice win
        """
        for c in s:
            if c in 'aeiou':
                return True

        return False
