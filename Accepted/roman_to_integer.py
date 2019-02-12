"""
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        refDict = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rslt = 0
        preNum = 0
        currNum = 0

        if len(s) == 0:
            return 0  # Empty string indicate number zero.

        for c in s:
            currNum = refDict.get(c)

            if currNum is None:
                return -1  # Negative number indicate transformation error.

            if currNum > preNum:  # Case IV, IX, XL, XC, CD, CM.
                rslt -= preNum * 2  # Subtract the previous number.

            rslt += currNum
            preNum = currNum

        return rslt


print(Solution().romanToInt('III'))
