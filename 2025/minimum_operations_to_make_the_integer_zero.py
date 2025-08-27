"""
https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description/
"""


class Solution:
    """
    Solution
    """

    def make_the_integer_zero(self, num1: int, num2: int) -> int:
        """
        make the integer zero
        """
        delta = num1
        for k in range(1, 61):
            delta -= num2
            if delta.bit_count() <= k <= delta:
                return k

        return -1


print(Solution().make_the_integer_zero(3, -2))
