"""
https://leetcode.com/problems/k-items-with-the-maximum-sum/description/
"""


class Solution:
    """
    Solution
    """

    def k_items_with_maximum_sum(
        self,
        num_ones: int,
        num_zeros: int,
        num_neg_ones: int,
        k: int
    ) -> int:
        """
        k item with maximum sum
        """
        if k <= num_ones:
            return k

        if k <= num_ones + num_zeros:
            return num_ones

        return (num_ones << 1) + num_zeros - k
