"""
https://leetcode.com/problems/number-of-pairs-satisfying-inequality/description/
"""


from bisect import bisect_right, insort_right


class Solution:
    """
    Solution
    """

    def number_of_pairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        """
        n1[i] - n1[j] <= n2[i] - n2[j] + diff ===>
        n1[i] - n2[i] <= n1[j] - n2[j] + diff ===> suppose c[i] = n1[i] - n2[i]
        c[i] <= c[j] + diff

        find those pairs (i, j) in c.
        """
        memo: list[int] = []
        pairs = 0

        for a, b in zip(nums1, nums2):
            d = a - b
            pairs += bisect_right(memo, d + diff)
            insort_right(memo, d)

        return pairs
