"""
https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/
"""


from functools import cache
from bisect import bisect_right, bisect_left


class Solution:
    """
    Solution
    """

    def full_bloom_flowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        """
        full bloom flowers
        """
        @cache
        def count(day: int) -> int:
            bloomed_flowers = bisect_right(bloom_starts, day)
            withered_flowers = bisect_left(bloom_ends, day)
            return bloomed_flowers - withered_flowers

        bloom_starts = sorted(start for start, _ in flowers)
        bloom_ends = sorted(end for _, end in flowers)
        return list(map(count, people))


print(Solution().full_bloom_flowers(
    [[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]))
