"""
https://leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or numRows > len(s):
            return s

        rowList = [''] * numRows
        row = top = 0
        bottom = numRows - 1

        # Visit by rows.
        for c in s:
            rowList[row] += c

            if row == top:
                offset = 1  # Going down

            if row == bottom:
                offset = -1  # Going up

            row += offset

        return ''.join(rowList)


# textList = [('PAYPALISHIRING', 3), ('PAYPALISHIRING', 4)]
textList = [('PAYPALISHIRING', 3), ('PAYPALISHIRING', 4)]
rsltList = ['PAHNAPLSIIGYIR', 'PINALSIGYAHRPI']
s = Solution()

for text in textList:
    rslt = s.convert(*text)
    print('{0} -> {1}'.format(text, rslt))
    print(rslt in rsltList)
