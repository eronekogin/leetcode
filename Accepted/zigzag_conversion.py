class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or numRows > len(s):
            return s

        workList = [''] * numRows
        index = 0

        # Visit by rows.
        for c in s:
            workList[index] += c

            if index == 0:
                direction = 1  # Going down
            elif index == numRows - 1:
                direction = -1  # Going up

            index += direction

        return ''.join(workList)


# textList = [('PAYPALISHIRING', 3), ('PAYPALISHIRING', 4)]
textList = [('PAYPALISHIRING', 3), ('PAYPALISHIRING', 4)]
rsltList = ['PAHNAPLSIIGYIR', 'PINALSIGYAHRPI']
s = Solution()

for text in textList:
    rslt = s.convert(*text)
    print('{0} -> {1}'.format(text, rslt))
    print(rslt in rsltList)
