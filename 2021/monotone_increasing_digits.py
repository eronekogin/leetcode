"""
https://leetcode.com/problems/monotone-increasing-digits/
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        currNum, digits = N, []
        while currNum:
            currNum, d = divmod(currNum, 10)
            digits.append(d)

        for i in range(len(digits) - 1):
            if digits[i] < digits[i + 1]:
                digits[:i + 1] = [9] * (i + 1)
                digits[i + 1] -= 1

        return sum(num * 10 ** i for i, num in enumerate(digits))


print(Solution().monotoneIncreasingDigits(100))
