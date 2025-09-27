"""
https://leetcode.com/problems/split-strings-by-separator/description/
"""


class Solution:
    """
    Solution
    """

    def split_words_by_separator(self, words: list[str], separator: str) -> list[str]:
        """
        split words by separator
        """
        rslt: list[str] = []
        for w in words:
            for x in w.split(separator):
                if len(x) > 0:
                    rslt.append(x)

        return rslt
