"""
https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
"""


from bisect import bisect_right
from itertools import accumulate


class Solution:
    """
    Solution
    """

    def answer_queries(self, nums: list[int], queries: list[int]) -> list[int]:
        """
        answer queries
        """
        prefix_sums = list(accumulate(sorted(nums)))
        return [bisect_right(prefix_sums, q) for q in queries]
