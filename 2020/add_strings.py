"""
https://leetcode.com/problems/add-strings/
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            return self.addStrings(num2, num1)

        rslt, carry = [], 0
        for i in range(-1, -len(num2) - 1, -1):
            carry, currDigit = divmod(int(num1[i]) + int(num2[i]) + carry, 10)
            rslt.append(str(currDigit))

        for i in range(i - 1, -len(num1) - 1, -1):
            if carry:
                carry, currDigit = divmod(int(num1[i]) + carry, 10)
                rslt.append(str(currDigit))
            else:
                rslt.append(num1[i])

        if carry:
            rslt.append(str(carry))

        return ''.join(reversed(rslt))


print(Solution().addStrings('9234', '789'))
