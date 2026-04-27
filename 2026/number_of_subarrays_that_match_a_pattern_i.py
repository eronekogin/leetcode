"""
https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/description/
"""


from itertools import pairwise


class Solution:
    """
    Solution
    """

    def count_matching_subarrays(self, nums: list[int], pattern: list[int]) -> int:
        """
        count mat ching subarrays
        """
        def f(x: tuple[int, int]) -> int:
            return (x[1] > x[0]) - (x[1] < x[0])

        n = len(nums)
        p = len(pattern)

        relatives = list(map(f, pairwise(nums)))
        return sum(
            relatives[i: i + p] == pattern
            for i in range(n - p + 1)
        )
