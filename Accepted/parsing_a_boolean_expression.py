"""
https://leetcode.com/problems/parsing-a-boolean-expression/
"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack: list[str] = []
        for c in expression:
            if c == ')':
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())

                stack.pop()  # Pop out '(' first.
                operator = stack.pop()
                if operator == '&':
                    stack.append(all(seen))
                elif operator == '|':
                    stack.append(any(seen))
                else:
                    stack.append(not seen.pop())
            elif c != ',':
                if c == 't':
                    stack.append(True)
                elif c == 'f':
                    stack.append(False)
                else:
                    stack.append(c)

        return stack.pop()
