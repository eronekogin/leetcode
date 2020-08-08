"""
https://leetcode.com/problems/base-7/
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        memo = '0123456789'
        nextNum = abs(num)
        rslt = []
        while nextNum:
            nextNum, currDigit = divmod(nextNum, 7)
            rslt.append(memo[currDigit])

        if num < 0:
            rslt.append('-')

        return ''.join(reversed(rslt))
