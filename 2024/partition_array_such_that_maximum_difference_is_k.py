"""
https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/
"""


class Solution:
    """
    Solution
    """

    def partition_array(self, nums: list[int], k: int) -> int:
        """
        it is optimal to put all numbers between min and max number of a
        sequence into this sequence.
        """
        sorted_nums = sorted(nums)
        start = sorted_nums[0]
        sequences = 1

        for end in sorted_nums:
            if end - start <= k:
                continue

            sequences += 1
            start = end

        return sequences
