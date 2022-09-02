"""
https://leetcode.com/problems/thousand-separator/
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1:
            return str(n)

        remain = n
        cnt = 0
        rslt: list[str] = []
        while remain:
            remain, r = divmod(remain, 10)
            cnt += 1
            rslt.append(str(r))
            if cnt % 3 == 0 and remain > 0:
                rslt.append('.')

        return ''.join(reversed(rslt))
