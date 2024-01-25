"""
https://leetcode.com/problems/intervals-between-identical-elements/description/
"""

from collections import defaultdict
from itertools import accumulate


class Solution:
    """
    Solution
    """

    def get_distances(self, arr: list[int]) -> list[int]:
        """
        get_distances
        """
        memo: defaultdict[int, list] = defaultdict(list)
        for i, x in enumerate(arr):
            memo[x].append(i)

        rslt = [0] * len(arr)
        for indexes in memo.values():
            n = len(indexes)
            pre_sums = [0] + list(accumulate(indexes))

            for i, v in enumerate(indexes):
                rslt[v] = (
                    (v * (i + 1) - pre_sums[i + 1]) +
                    (pre_sums[n] - pre_sums[i]) - v * (n - i)
                )

        return rslt
