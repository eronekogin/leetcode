"""
https://leetcode.com/problems/find-words-containing-character/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def find_words_containing(self, words: list[str], x: str) -> list[int]:
        """
        Docstring for find_words_containing

        :param self: Description
        :param words: Description
        :type words: list[str]
        :param x: Description
        :type x: str
        :return: Description
        :rtype: list[int]
        """
        return [
            i
            for i, w in enumerate(words)
            if x in set(w)
        ]
