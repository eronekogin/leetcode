"""
https://leetcode.com/problems/count-the-number-of-square-free-subsets/description/
"""


from collections import Counter
from math import gcd


class Solution:
    """
    Solution
    """

    def square_free_subsets(self, nums: list[int]) -> int:
        """
        square free subsets
        """
        def calc(curr_nums: list[int]) -> int:
            if not curr_nums:
                return 1

            t = curr_nums[0]
            next_nums = [
                x
                for x in curr_nums
                if gcd(x, t) == 1
            ]

            return (
                calc(curr_nums[1:]) +
                freqs[t] * calc(next_nums)
            ) % m

        freqs = Counter(nums)
        m = 10 ** 9 + 7
        candidates = [
            2, 3, 5, 6, 7,
            10, 11, 13, 14, 15,
            17, 19, 21, 22, 23,
            26, 29, 30
        ]

        return (calc(candidates) * pow(2, freqs[1], m) - 1) % m
