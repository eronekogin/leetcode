"""
https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/description/
"""


class Solution:
    """
    Solution
    """

    def minimize_tesult(self, expression: str) -> str:
        """
        minimize result
        """
        pivot = expression.index('+')
        n = len(expression)
        min_rslt = float('inf')
        min_expression = ''

        for l in range(pivot):
            left_multiplier = int(expression[:l]) if l else 1
            left_adder = int(expression[l: pivot])

            for r in range(pivot + 2, n + 1):
                right_adder = int(expression[pivot + 1: r])
                right_multiplier = int(expression[r: n]) if r < n else 1

                curr_rslt = (
                    left_multiplier *
                    (left_adder + right_adder) *
                    right_multiplier
                )

                if curr_rslt < min_rslt:
                    min_rslt = curr_rslt
                    min_expression = (
                        expression[:l] +
                        '(' + expression[l: r] + ')' + expression[r:]
                    )

        return min_expression


print(Solution().minimize_tesult('247+38'))
