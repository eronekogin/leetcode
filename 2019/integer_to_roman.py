"""
https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    def intToRoman(self, num: 'int') -> 'str':
        refDict = {1: ('I', 'V'), 2: ('X', 'L'), 3: ('C', 'D'), 4: ('M', None)}
        rsltList = []
        cnt = 0

        while num > 0:
            chkNum = num % 10
            num //= 10
            cnt += 1

            if refDict[cnt][1] is None and chkNum >= 4:
                return 'Input number should not exceed 3999.'

            if chkNum < 4:
                rsltList.append(refDict[cnt][0] * chkNum)
            elif chkNum == 4:
                rsltList.append(refDict[cnt][0] + refDict[cnt][1])
            elif chkNum == 5:
                rsltList.append(refDict[cnt][1])
            elif chkNum < 9:
                rsltList.append(
                    refDict[cnt][1] + (refDict[cnt][0] * (chkNum - 5)))
            else:
                rsltList.append(refDict[cnt][0] + refDict[cnt + 1][0])

        rsltList.reverse()
        return ''.join(rsltList)
