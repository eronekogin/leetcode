"""
https://leetcode.com/problems/basic-calculator-ii/
"""


class Solution:
    def calculate(self, s: str) -> int:
        operator, operand, stack = '+', 0, []
        for c in s + '+':  # Make sure the last number is processed.
            if c == ' ':
                continue

            if c.isdigit():
                operand = operand * 10 + int(c)
                continue

            # Found a new operator, process the previous operation first.
            if operator == '+':
                stack.append(operand)
            elif operator == '-':
                stack.append(-operand)
            elif operator == '*':
                stack.append(stack.pop() * operand)
            else:
                pre = stack.pop()
                if pre >= 0:
                    stack.append(pre // operand)
                else:
                    stack.append(-(-pre // operand))  # Round toward zero.

            operand, operator = 0, c

        return sum(stack)


print(Solution().calculate('3+2*2'))
