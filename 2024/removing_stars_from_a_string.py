"""
https://leetcode.com/problems/removing-stars-from-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def remove_stars(self, s: str) -> str:
        """
        remove stars
        """
        stack: list[str] = []
        for c in s:
            if c != '*':
                stack.append(c)
                continue

            if stack:
                stack.pop()

        return ''.join(stack)
