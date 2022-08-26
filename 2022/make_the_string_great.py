"""
https://leetcode.com/problems/make-the-string-great/
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack: list[str] = []
        for c in s:
            if stack and stack[-1] != c and stack[-1].lower() == c.lower():
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
