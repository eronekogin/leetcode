"""
https://leetcode.com/problems/sum-of-distances/description/
"""


from collections import defaultdict
from itertools import accumulate


class Solution:
    """
    Solution
    """

    def distance(self, nums: list[int]) -> list[int]:
        """
        distance
        """
        memo = defaultdict(list)
        for i, x in enumerate(nums):
            memo[x].append(i)

        rslt: list[int] = [0] * len(nums)
        for v in memo.values():
            pre_sums = list(accumulate(v))
            total = sum(v)
            n = len(v)

            for j, i in enumerate(v):
                rslt[i] = (
                    total +
                    (2 * j + 2 - n) * i -
                    2 * pre_sums[j]
                )

        return rslt


print(Solution().distance([1, 3, 1, 1, 2]))
