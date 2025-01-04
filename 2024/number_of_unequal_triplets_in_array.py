"""
https://leetcode.com/problems/number-of-unequal-triplets-in-array/description/
"""


class Solution:
    """
    Solution
    """

    def unequal_triplets(self, nums: list[int]) -> int:
        """
        unequal triplets
        """
        triplets = pairs = 0
        freqs = {}
        for i, x in enumerate(nums):
            fx = freqs.get(x, 0)
            pairs_with_a = i - fx
            triplets += pairs - fx * pairs_with_a
            pairs += i - fx
            freqs[x] = fx + 1

        return triplets
