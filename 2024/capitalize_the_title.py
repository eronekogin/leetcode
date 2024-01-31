"""
https://leetcode.com/problems/capitalize-the-title/description/
"""


class Solution:
    """
    Solution
    """

    def capitalize_title(self, title: str) -> str:
        """
        capitalize_title
        """
        words = title.split()
        for i, w in enumerate(words):
            if len(w) <= 2:
                words[i] = w.lower()
            else:
                words[i] = w.title()

        return ' '.join(words)
