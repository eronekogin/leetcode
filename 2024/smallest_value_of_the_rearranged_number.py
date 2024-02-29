"""
https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/
"""


class Solution:
    """
    Solution
    """

    def smallest_number(self, num: int) -> int:
        """
        smallest number
        """
        if num == 0:
            return num

        digits = list(str(abs(num)))

        digits.sort()
        n = len(digits)

        if num > 0:
            start = end = 0
            while end < n and digits[end] == '0':
                end += 1

            digits[start], digits[end] = digits[end], digits[start]
            return int(''.join(digits))

        # num < 0
        start = end = n - 1
        while end >= 0 and digits[end] == '0':
            end -= 1

        digits[start], digits[end] = digits[end], digits[start]
        return int(''.join(reversed(digits))) * -1
