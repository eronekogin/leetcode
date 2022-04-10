"""
https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == 'c':
                if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return not stack


print(Solution().isValid("abacbcabcc"))
