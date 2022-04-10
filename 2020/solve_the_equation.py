"""
https://leetcode.com/problems/solve-the-equation/
"""


from typing import Tuple


class Solution:
    def solveEquation(self, equation: str) -> str:
        def get_coefficient_and_constant(s: str) -> Tuple[int, int]:
            if s[0] == '-':
                sign = -1
                t = s[1:] + '+'
            else:
                sign = 1
                t = s + '+'

            start, coefficient, constant, operators = 0, 0, 0, set('+-')
            for end, c in enumerate(t):
                if c in operators:
                    if t[end - 1] == 'x':  # Calculate coefficient.
                        if start == end - 1:
                            coefficient += sign
                        else:
                            coefficient += int(t[start: end - 1]) * sign
                    else:  # Calculate constant.
                        constant += int(t[start: end]) * sign

                    start = end + 1
                    if c == '+':
                        sign = 1
                    else:
                        sign = -1

            return (coefficient, constant)

        left, right = equation.split('=')
        lCoefficient, lConstant = get_coefficient_and_constant(left)
        rCoefficient, rConstant = get_coefficient_and_constant(right)
        coefficient = lCoefficient - rCoefficient
        constant = rConstant - lConstant

        if not coefficient:
            if not constant:
                return 'Infinite solutions'
            else:
                return 'No solution'

        if constant % coefficient:
            return 'No solution'

        return 'x={0}'.format(constant // coefficient)


print(Solution().solveEquation('x+5-3+x=6+x-2'))
