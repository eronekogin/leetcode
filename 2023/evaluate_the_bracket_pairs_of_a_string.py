"""
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
"""


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        words = {k: v for k, v in knowledge}
        rslt = []
        start = 0
        end, n = 0, len(s)

        while end < n:
            if s[end] == '(':
                start = end
                while end < n and s[end] != ')':
                    end += 1

                key = s[start + 1: end]
                v = words.get(key, '?')
            else:
                v = s[end]

            rslt.append(v)
            end += 1

        return ''.join(rslt)
