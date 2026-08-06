"""
https://leetcode.com/problems/clear-digits/description/
"""


class Solution:
    """
    Solution
    """

    def clear_digits(self, s: str) -> str:
        """
        clear digits
        """
        stack: list[str] = []
        for c in s:
            if not c.isnumeric():
                stack.append(c)
                continue

            if not stack:
                stack.append(c)
            else:
                if stack[-1].isnumeric():
                    stack.append(c)
                else:
                    stack.pop()

        return ''.join(stack)
