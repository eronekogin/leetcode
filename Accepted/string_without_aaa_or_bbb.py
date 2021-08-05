"""
https://leetcode.com/problems/string-without-aaa-or-bbb/
"""


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a == b:
            return 'ab' * a
        elif a < b:
            n1, r1 = divmod(b, 2)
            n2 = a
            rslt = ['bb'] * n1 + ['b'] * r1
            padChar = 'a'
        else:
            n1, r1 = divmod(a, 2)
            n2 = b
            rslt = ['aa'] * n1 + ['a'] * r1
            padChar = 'b'

        while n2 > 0:
            for i in range(n1):
                if n2 > 0:
                    rslt[i] += padChar
                    n2 -= 1
                else:
                    break

        return ''.join(rslt)


print(Solution().strWithout3a3b(1, 1))
