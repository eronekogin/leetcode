"""
https://leetcode.com/problems/reformat-the-string/
"""


class Solution:
    def reformat(self, s: str) -> str:
        if len(s) < 2:
            return s

        digits: list[str] = []
        chars: list[str] = []
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                chars.append(c)

        maxLen = max(len(digits), len(chars))
        rslt = [d + c for d, c in zip(digits, chars)]
        if len(rslt) < maxLen - 1:
            return ''

        if len(digits) > len(chars):
            return ''.join(rslt + [digits[-1]])
        elif len(digits) == len(chars):
            return ''.join(rslt)
        else:
            return ''.join([chars[-1]] + rslt)


print(Solution().reformat('covid2019'))
