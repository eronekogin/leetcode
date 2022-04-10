"""
https://leetcode.com/problems/basic-calculator-iv/
"""


from typing import List


from collections import Counter


class Poly(Counter):
    """
    Stands for a polynomial parsed from an expression:

    1. Each key stands for a variable and the key is a tuple. For example, if
        the variable is a*b*b*c then the key is (a, b, b, c).
    2. Each value stands for its coefficient.
    """

    def __add__(self, other: 'Poly') -> 'Poly':
        self.update(other)
        return self

    def __sub__(self, other: 'Poly') -> 'Poly':
        self.update({k: -v for k, v in other.items()})
        return self

    def __mul__(self, other: 'Poly') -> 'Poly':
        rslt = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                rslt.update({tuple(sorted(k1 + k2)): v1 * v2})

        return rslt

    def evaluate(self, evalMap: dict[str, int]) -> 'Poly':
        """
        Evaulate the current polynomial by replacing any matching variable
        names with its mapping constants, then return the evaulated polynomial.
        """
        rslt = Poly()
        for k, v in self.items():
            noMappingVars = []
            for varName in k:
                if varName in evalMap:
                    v *= evalMap[varName]
                else:
                    noMappingVars.append(varName)

            rslt[tuple(noMappingVars)] += v

        return rslt

    def to_list(self) -> List[str]:
        """
        Return the target format of the current polynomial, where the longest
        variable names come first. When the coefficient is zero, do not put it
        to the output.
        """
        return [
            '*'.join((str(v), ) + k)
            for k, v in sorted(self.items(), key=lambda x: (-len(x[0]), x[0]))
            if v]


class Solution:
    OPS = set('+-*')

    def _calc(self, l: Poly, r: Poly, oper: str) -> Poly:
        """
        Calculate the result between two polynomials.
        """
        if oper == '+':
            return l + r
        elif oper == '-':
            return l - r
        else:
            return l * r

    def _create(self, expr: str) -> Poly:
        """
        Create a new poly from an expression.
        """
        rslt = Poly()
        if expr.isdigit():
            rslt[()] = int(expr)
        else:
            rslt[(expr, )] = 1

        return rslt

    def _parse(self, expr: str) -> Poly:
        """
        Parse an expression into a poly.
        """
        tokens, operators = [], []
        i, N = 0, len(expr)
        while i < N:  # Parse expression into tokens first.
            if expr[i] == '(':
                cnt = 1  # Count Parentheses.
                j = i
                while j + 1 < N and cnt:
                    j += 1
                    if expr[j] == '(':
                        cnt += 1
                    elif expr[j] == ')':
                        cnt -= 1

                tokens.append(self._parse(expr[i + 1: j]))
                i = j
            elif expr[i].isalnum():
                j = i + 1
                while j < N and expr[j] != ' ':
                    j += 1

                tokens.append(self._create(expr[i: j]))
                i = j
            elif expr[i] in self.OPS:
                operators.append(expr[i])

            i += 1

        # Multiply takes precedence over add and subtract. So we calculate
        # multiply first.
        for i in reversed(range(len(operators))):
            if operators[i] == '*':
                tokens[i] = self._calc(
                    tokens[i], tokens.pop(i + 1), operators.pop(i))

        # Now calculate the add and subtract.
        rslt = tokens[0]
        for token, operator in zip(tokens[1:], operators):
            rslt = self._calc(rslt, token, operator)

        return rslt

    def basicCalculatorIV(
            self,
            expression: str,
            evalvars: List[str],
            evalints: List[int]) -> List[str]:
        evalMap = dict(zip(evalvars, evalints))
        return self._parse(expression).evaluate(evalMap).to_list()


print(Solution().basicCalculatorIV(
    "(e + 8) * (e - 8)",
    [],
    []
))
