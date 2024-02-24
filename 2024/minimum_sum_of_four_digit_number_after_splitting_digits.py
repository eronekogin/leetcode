"""
https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_sum(self, num: int) -> int:
        """
        minimum_sum
        """
        digits = [int(c) for c in str(num)]
        digits.sort()
        return digits[0] * 10 + digits[1] * 10 + digits[2] + digits[3]
