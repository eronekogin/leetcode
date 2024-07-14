"""
https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/
"""


class Solution:
    """
    Solution
    """

    def greatest_letter(self, s: str) -> str:
        """
        greatest letter
        """
        memo = set(s)
        max_char = ''
        visited: set[str] = set()

        for w in s:
            if w.lower() in visited:
                continue

            if w.lower() in memo and w.upper() in memo:
                max_char = max(max_char, w.upper())

            visited.add(w.lower())

        return max_char
