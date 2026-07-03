"""
https://leetcode.com/problems/minimum-array-end/description/
"""


class Solution:
    """
    Solution
    """

    def min_end(self, n: int, x: int) -> int:
        """
        Each number in the result array should have the
        same or more set bit as x so that their bitwise
        and result will be x

        Then we can check how many remaining steps we need
        to form the last element of the array and to make
        it a minimum one, we are adding the binary format
        of remain_step to unset bit of x.
        """
        rslt = x
        remain_step = n - 1
        mask = 1

        while remain_step:
            if (mask & x) == 0:
                rslt |= (remain_step & 1) * mask
                remain_step >>= 1

            mask <<= 1

        return rslt
