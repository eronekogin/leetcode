"""
https://leetcode.com/problems/fraction-addition-and-subtraction/
"""


from fractions import Fraction


class Solution:
    def fractionAddition(self, expression: str) -> str:
        rslt, start = 0, 0
        if expression[0] == '-':
            sign = -1
            expr = expression[1:] + '+'
        else:
            sign = 1
            expr = expression + '+'

        for end, c in enumerate(expr):
            if c == '+' or c == '-':
                n, d = expr[start: end].split('/')
                f = Fraction(int(n), int(d))
                rslt += f * sign
                start = end + 1
                if c == '+':
                    sign = 1
                else:
                    sign = -1

        return '{0}/{1}'.format(rslt.numerator, rslt.denominator)


print(Solution().fractionAddition('-1/2+1/2'))
