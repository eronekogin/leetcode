"""
https://leetcode.com/problems/find-the-array-concatenation-value/description/
"""


class Solution:
    """
    Solution
    """

    def find_the_array_conc_val(self, nums: list[int]) -> int:
        """
        find the array con val
        """
        def calc(left: int, right: int) -> int:
            rslt = left
            right_digits = []
            while right:
                right, r = divmod(right, 10)
                right_digits.append(r)

            for d in reversed(right_digits):
                rslt = rslt * 10 + d

            return rslt

        rslt = 0
        l, r = 0, len(nums) - 1
        while l < r:
            rslt += calc(nums[l], nums[r])
            l += 1
            r -= 1

        if l == r:
            return rslt + nums[l]

        return rslt
