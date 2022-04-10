"""
https://leetcode.com/problems/multiply-strings/
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m, n, delta = len(num1), len(num2), ord('0')
        rslt = [0] * (m + n)  # Initialize result.

        for i in range(m - 1, -1, -1):
            a = ord(num1[i]) - delta

            for j in range(n - 1, -1, -1):
                # For each [i, j], the num1[i] * num2[j] will be
                # stored at rslt[i + j, i + j + 1], while
                # rslt[i + j + 1] stores the ones digit and
                # rslt[i + j] stores the tens digit.
                b = ord(num2[j]) - delta
                carry = rslt[i + j + 1] + a * b
                rslt[i + j] += carry // 10
                rslt[i + j + 1] = carry % 10

        # Convert remaining string.
        for i in range(m + n):
            rslt[i] = chr(rslt[i] + delta)

        return ''.join(rslt).lstrip('0')


num1, num2 = '0', '0'
print(Solution().multiply(num1, num2))
