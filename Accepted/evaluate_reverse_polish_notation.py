"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rslt, operators = [], {'+', '-', '*', '/'}
        for token in tokens:
            if token not in operators:
                rslt.append(int(token))
            else:
                y = rslt.pop()
                x = rslt.pop()
                if token == '+':
                    rslt.append(x + y)
                elif token == '-':
                    rslt.append(x - y)
                elif token == '*':
                    rslt.append(x * y)
                else:
                    rslt.append(int(x / y))  # Truncate toward zero.

        return rslt.pop()


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))
