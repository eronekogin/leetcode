"""
https://leetcode.com/problems/maximum-odd-binary-number/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_odd_binary_number(self, s: str) -> str:
        """
        maximum odd binary number
        """
        ones = zeros = 0
        for c in s:
            if c == '0':
                zeros += 1
            else:
                ones += 1

        return (ones - 1) * '1' + '0' * zeros + '1'
