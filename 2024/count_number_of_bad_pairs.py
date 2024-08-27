"""
https://leetcode.com/problems/count-number-of-bad-pairs/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_bad_pairs(self, nums: list[int]) -> int:
        """
        count bad pairs
        """
        cnt = Counter(x - i for i, x in enumerate(nums))
        good_pairs = sum((v * (v - 1)) >> 1 for v in cnt.values())
        n = len(nums)
        return ((n * (n - 1)) >> 1) - good_pairs
