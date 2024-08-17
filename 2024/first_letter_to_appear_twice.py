"""
https://leetcode.com/problems/first-letter-to-appear-twice/description/
"""


class Solution:
    """
    Solution
    """

    def repeated_character(self, s: str) -> str:
        """
        repeated character
        """
        visited: set[str] = set()
        for c in s:
            if c in visited:
                return c

            visited.add(c)

        return ''
