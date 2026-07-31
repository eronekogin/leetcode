"""
https://leetcode.com/problems/find-the-number-of-good-pairs-ii/description/
"""

from collections import Counter


class Solution:
    """
    Solution
    """

    def number_of_pairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        number of pairs
        """
        c2 = Counter([x * k for x in nums2])
        cnt = [0] * (max(nums1) + 1)

        for k, v in c2.items():
            for x in range(k, len(cnt), k):
                cnt[x] += v

        return sum(cnt[x] for x in nums1)
