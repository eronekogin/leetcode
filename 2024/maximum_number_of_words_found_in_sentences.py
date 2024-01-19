"""
https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
"""


class Solution:
    """
    Solution
    """

    def most_words_found(self, sentences: list[str]) -> int:
        """
        most_words_found
        """
        return max(len(s.split()) for s in sentences)
