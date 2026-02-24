"""
https://leetcode.com/problems/remove-adjacent-almost-equal-characters/description/
"""


class Solution:
    """
    Solution
    """

    def remove_almost_equal_characters(self, word: str) -> int:
        """
        remove almost equal characters
        """
        i = 1
        ops = 0

        while i < len(word):
            if abs(ord(word[i]) - ord(word[i - 1])) < 2:
                ops += 1  # Need replace
                i += 1  # Skip i + 1 since already handled

            i += 1

        return ops
