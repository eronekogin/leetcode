"""
https://leetcode.com/problems/score-of-parentheses/
"""


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                score = 0
                while stack[-1] != '(':
                    score += stack.pop()

                stack.pop()  # Pop the previous '('.
                if not score:  # Case '()'
                    stack.append(1)
                else:
                    stack.append(score * 2)

        return sum(stack)


print(Solution().scoreOfParentheses("(()(()))"))
