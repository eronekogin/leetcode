"""
https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/
"""


class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        """
        Base patterns:

            1. ...?(...)
            2. ...?n

            where ? stands for operator & or |, n stands for 0 or 1, ... stands for recurcive patterns.
        """
        def dfs(start: int, end: int):
            if start == end:  # Just n.
                return (int(expression[start]), 1)
            
            m = bracktPositions.get(end, end)
            if m == start:  # Start and end is a pair of brackets.
                return dfs(start + 1, end - 1)

            p1, c1 = dfs(start, m - 2)  # Process left part.
            p2, c2 = dfs(m, end)  # Process right part.
            oper = expression[m - 1]

            patterns = {
                '|': lambda x, y: x | y,
                '&': lambda x, y: x & y
            }

            if p1 + p2 == 1:
                c3 = 1
            else:
                c3 = min(c1, c2) + (p1 ^ (oper == '&'))
            
            return (patterns[oper](p1, p2), c3)

        # Calculate parenthesis opening and closing indexes.
        bracktPositions: dict[int, int] = {}
        stack: list[int] = []
        for i, c in enumerate(expression):
            if c == '(':
                stack.append(i)
            elif c == ')':
                bracktPositions[i] = stack.pop()
        
        return dfs(0, len(expression) - 1)[1]