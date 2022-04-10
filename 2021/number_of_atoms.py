"""
https://leetcode.com/problems/number-of-atoms/
"""


from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i, N = 0, len(formula)
        stack = [Counter()]
        while i < N:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                cnt = stack.pop()
                i += 1
                digitStart = i
                while i < N and formula[i].isdigit():
                    i += 1

                dupTimes = int(formula[digitStart: i] or 1)
                for name in cnt:
                    stack[-1][name] += cnt[name] * dupTimes
            else:
                nameStart = i
                i += 1
                while i < N and formula[i].islower():
                    i += 1

                name = formula[nameStart: i]

                digitStart = i
                while i < N and formula[i].isdigit():
                    i += 1

                dupTimes = int(formula[digitStart: i] or 1)
                stack[-1][name] += dupTimes

        return ''.join(
            sorted(k + str(v) if v > 1 else k for k, v in stack[-1].items()))


print(Solution().countOfAtoms('H2O'))
