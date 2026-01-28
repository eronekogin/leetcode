"""
https://leetcode.com/problems/maximum-balanced-subsequence-sum/description/
"""


from bisect import bisect_right
from math import inf


class Solution:
    """
    Docstring for Solution
    """

    def max_balanced_subsequence_sum(self, nums: list[int]) -> int:
        """
        Docstring for max_balanced_subsequence_sum

        :param self: Description
        :param nums: Description
        :type nums: list[int]
        :return: Description
        :rtype: int
        """
        m = [(-inf, 0)]

        for i, x in enumerate(nums):
            if x > 0:
                p = bisect_right(m, (x - i, inf))
                m.insert(p, (x - i,  x + m[p - 1][1]))

                while p + 1 < len(m) and m[p + 1][1] < m[p][1]:
                    del m[p + 1]

        if len(m) > 1:
            return m[-1][1]

        return max(nums)
