"""
https://leetcode.com/problems/sum-of-number-and-its-reverse/description/
"""


class Solution:
    """
    Solution
    """

    def sum_of_number_and_reverse(self, num: int) -> bool:
        """
        There is always a number which will be greater than the half of num
        if there is a candidate.
        """
        for x in range((num >> 1), num + 1):
            if x + int(str(x)[::-1]) == num:
                return True

        return False
