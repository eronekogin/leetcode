"""
https://leetcode.com/problems/most-frequent-even-element/description/
"""


class Solution:
    """
    Solution
    """

    def most_frequent_even(self, nums: list[int]) -> int:
        """
        most frequent even
        """
        max_num = -1
        max_cnt = -1
        memo = {}
        for x in nums:
            if x & 1:
                continue

            memo[x] = memo.get(x, 0) + 1
            if (
                memo[x] > max_cnt or
                (memo[x] == max_cnt and x < max_num)
            ):
                max_num = x
                max_cnt = memo[x]

        return max_num
