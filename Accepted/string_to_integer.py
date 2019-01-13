"""
https://leetcode.com/problems/string-to-integer-atoi/
"""


class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = len(s)
        if total == 0:
            return 0

        chkDict = dict([(str(x), x) for x in range(10)])
        CHKINT = ((1 << 31) - 1) // 10

        i = 0

        # Strip leading blanks.
        while i < total and s[i] == ' ':
            i += 1

        if i == total:
            return 0  # String contains all blank

        # Check optional sign char.
        if chkDict.get(s[i]) is None:
            if s[i] == '+':
                neg = False
            elif s[i] == '-':
                neg = True
            else:
                return 0  # No valid num sequence

            i += 1
            if i == total or chkDict.get(s[i]) is None:
                return 0  # No valid num sequence
        else:
            neg = False  # If no sign char, default to positive number

        # Processing digits.
        rslt = 0
        overflow = False
        while i < total:
            t = chkDict.get(s[i])

            if t is None:
                break  # Completed processing digits

            # Check overflow.
            if rslt > CHKINT:
                overflow = True
                break

            if rslt == CHKINT:
                if (neg and t > 8) or (not neg and t > 7):
                    overflow = True
                    break

            rslt = rslt * 10 + t
            i += 1

        if overflow:
            if neg:
                return -(1 << 31)
            else:
                return (1 << 31) - 1

        if neg:
            return -1 * rslt
        else:
            return rslt


print(Solution().myAtoi('-123'))
