"""
https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def number_of_pairs(self, nums: list[int]) -> list[int]:
        """
        number of pairs
        """
        pairs = remain = 0
        for v in Counter(nums).values():
            q, r = divmod(v, 2)
            pairs += q
            remain += r

        return [pairs, remain]
