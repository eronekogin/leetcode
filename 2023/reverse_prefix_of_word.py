"""
https://leetcode.com/problems/reverse-prefix-of-word/
"""


class Solution:
    """
    Solution
    """

    def reverse_prefix(self, word: str, ch: str) -> str:
        """
        reverse_prefix
        """
        for i, c in enumerate(word):
            if c == ch:
                return word[i::-1] + word[i + 1:]

        return word
