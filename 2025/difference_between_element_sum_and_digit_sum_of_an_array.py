"""
https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def difference_of_sum(self, nums: list[int]) -> int:
        """
        difference of sum
        """
        def sum_digits(x: int) -> int:
            rslt = 0
            while x:
                x, r = divmod(x, 10)
                rslt += r

            return rslt

        element_sum = digit_sum = 0
        for x in nums:
            element_sum += x
            digit_sum += sum_digits(x)

        return abs(element_sum - digit_sum)
