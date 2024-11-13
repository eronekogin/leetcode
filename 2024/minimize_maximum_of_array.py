"""
https://leetcode.com/problems/minimize-maximum-of-array/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def minimize_array_value(self, nums: list[int]) -> int:
        """
        Decrease a[i] and increase a[i - 1] by 1 means to move 1 from a[i]
        to a[i - 1] and it does not impact the total sum to a[i].

        Our goal is to move a[i] to a[i - 1] until a[i - 1] >= a[i], so
        ceil(avg(sum)) will be our result.

        ceil(a/b) = (a + b - 1) / b

        so ceil(avg(sum)) = ceil(sum / (i + 1)) = (sum + i) / (i + 1)
        """
        return max(
            (a + i) // (i + 1)
            for i, a in enumerate(accumulate(nums))
        )
