"""
https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/
"""


class Solution:
    """
    Solution
    """

    def min_element(self, nums: list[int]) -> int:
        """
        min element
        """
        def sum_digits(x: int) -> int:
            rslt = 0
            while x:
                x, r = divmod(x, 10)
                rslt += r

            return rslt

        return min(sum_digits(x) for x in set(nums))
