"""
https://leetcode.com/problems/count-the-number-of-good-partitions/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_good_partitions(self, nums: list[int]) -> int:
        """
        * All the same integers should exist in the same subarray
        * So if the current index > last index of the current number,
            we can either start a new subarray, or continue the existing
            subarray, which makes two options, so we double the
            current subarray counter
        """
        last = {x: i for i, x in enumerate(nums)}
        cnt = 1
        m = 10 ** 9 + 7
        j = 0

        for i, x in enumerate(nums):
            if i > j:
                cnt = (cnt * 2) % m

            j = max(j, last[x])

        return cnt
