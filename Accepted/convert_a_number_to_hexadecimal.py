"""
https://leetcode.com/problems/convert-a-number-to-hexadecimal/
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        hexChars = '0123456789abcdef'
        rslt = []
        if num < 0:
            q = num + (1 << 32)
        else:
            q = num

        while q:
            q, r = divmod(q, 16)
            rslt.append(hexChars[r])

        return ''.join(reversed(rslt))


print(Solution().toHex(-10))
