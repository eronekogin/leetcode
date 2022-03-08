"""
https://leetcode.com/problems/maximum-69-number/
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        rslt = list(str(num))
        for i, c in enumerate(rslt):
            if c == '6':
                rslt[i] = '9'
                break

        return int(''.join(rslt))
