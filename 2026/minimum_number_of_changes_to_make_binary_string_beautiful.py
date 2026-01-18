"""
https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def min_changes(self, s: str) -> int:
        """
        For each even group, it can be divided into smallest groups
        with two characters, so we can simply check such consecutive
        smallest groups and if the next one is not equal to the current,
        we just need 1 change to make the current group equal.
        """
        if len(s) & 1:
            return -1

        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))


print(Solution().min_changes('11000111'))
