"""
https://leetcode.com/problems/basic-calculator/
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack, operand, sign, rslt = [], 0, 1, 0
        for c in s + '+':  # Make sure the last number is processed.
            if c.isdecimal():  # '0' ~ '9'.
                operand = operand * 10 + int(c)
            elif c == '+':
                rslt += sign * operand
                operand, sign = 0, 1
            elif c == '-':
                rslt += sign * operand
                operand, sign = 0, -1
            elif c == '(':
                stack.append(rslt)
                stack.append(sign)
                rslt, sign = 0, 1
            elif c == ')':
                rslt += sign * operand
                rslt *= stack.pop()  # First poped is the sign.
                rslt += stack.pop()  # Then poped is the operand.
                operand = 0

        return rslt


print(Solution().calculate("12 + 34"))
