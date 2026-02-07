"""
https://leetcode.com/problems/separate-black-and-white-balls/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def minimum_steps(self, s: str) -> int:
        """
        Docstring for minimum_steps

        :param self: Description
        :param s: Description
        :type s: str
        :return: Description
        :rtype: int
        """
        prev_black_balls = 0
        swaps = 0
        for c in s:
            if c == '0':
                swaps += prev_black_balls
            else:
                prev_black_balls += 1

        return swaps
