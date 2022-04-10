"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        rslt = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:  # No previous '('.
                    rslt += 1
                else:
                    stack.pop()

        return rslt + len(stack)  # Add ')' for remaining unmatched '('.
