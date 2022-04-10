"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ')':
                rslt = []
                while stack and stack[-1] != '(':
                    rslt.append(stack.pop())

                if stack:  # Pop out '('.
                    stack.pop()

                stack.extend(rslt)
            else:
                stack.append(c)

        return ''.join(stack)


print(Solution().reverseParentheses("(u(love)i)"))
