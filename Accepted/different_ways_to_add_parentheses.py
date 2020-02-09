"""
https://leetcode.com/problems/different-ways-to-add-parentheses/
"""


from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        memo = {}

        def compare(target: str) -> List[int]:
            if target.isdecimal():  # Assume all numbers are integers.
                return [int(target)]

            if target in memo:
                return memo[target]

            rslt = []
            for i, c in enumerate(target):
                if target[i] in '+-*':
                    left, right = compare(target[:i]), compare(target[i + 1:])
                    for l in left:
                        for r in right:
                            if c == '+':
                                rslt.append(l + r)
                            elif c == '-':
                                rslt.append(l - r)
                            else:
                                rslt.append(l * r)

            memo[target] = rslt
            return rslt

        return compare(input)
