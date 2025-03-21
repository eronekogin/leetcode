"""
https://leetcode.com/problems/separate-the-digits-in-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def separate_digits(self, nums: list[int]) -> list[int]:
        """
        separate digits
        """
        rslt: list[int] = []
        for x in reversed(nums):
            while x:
                x, r = divmod(x, 10)
                rslt.append(r)

        return rslt[::-1]
