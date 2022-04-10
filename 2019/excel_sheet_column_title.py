"""
https://leetcode.com/problems/excel-sheet-column-title/
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        rslt, q = '', n
        while q:
            q, r = divmod(q, 26)
            if not r:  # r == 0.
                q -= 1
                rslt = 'Z' + rslt
            else:
                rslt = chr(ord('A') + r - 1) + rslt

        return rslt


print(Solution().convertToTitle(703))
