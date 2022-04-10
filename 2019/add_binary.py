"""
https://leetcode.com/problems/add-binary/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        delta = len(a) - len(b)
        if delta < 0:
            return self.addBinary(b, a)

        carry, rslt = 0, [0] * delta + list(b)
        for i in range(len(a)):
            newVal = int(rslt[~i]) + int(a[~i]) + carry
            carry = newVal // 2
            rslt[~i] = str(newVal % 2)

        if carry:
            return ''.join(['1'] + rslt)

        return ''.join(rslt)


print(Solution().addBinary('100', '110010'))
