"""
https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
"""


class Solution:
    """
    Solution
    """

    def min_length(self, s: str) -> int:
        """
        min length
        """
        stack: list[str] = []
        for c in s:
            if not stack:
                stack.append(c)
                continue

            if c == 'D' and stack[-1] == 'C':
                stack.pop()
            elif c == 'B' and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append(c)

        return len(stack)
