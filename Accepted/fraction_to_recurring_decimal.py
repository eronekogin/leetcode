"""
https://leetcode.com/problems/fraction-to-recurring-decimal/
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator:
            return '0'

        if not denominator:
            return None

        result = []
        # Determine the sign of the result.
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        n, d = abs(numerator), abs(denominator)
        q, r = divmod(n, d)
        result.append(str(q))

        if not r:  # No digit part.
            return ''.join(result)

        result.append('.')  # Has digit part.
        memo = {}
        while r:
            if r in memo:  # Remainder starts to loop.
                result.insert(memo[r], '(')
                result.append(')')
                break

            memo[r] = len(result)
            q, r = divmod(r * 10, d)
            result.append(str(q))

        return ''.join(result)
