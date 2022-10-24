"""
https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
"""


from math import comb


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        The question equals to calculate the number of ways to
        pick 2k different points from n + k - 1 points.

        Case 1: given n points, find k segments that allows end point sharing.

        Case 2: given n + k - 1 points, find k segments that does not allow
        end point sharing.

        Say we find a solution for case 2, then we could remove the internal
        points from any two consecutive segment to get solution for case 1,
        same as case 1 to case 2.
        """
        return comb(n + k - 1, k << 1) % (10 ** 9 + 7)
