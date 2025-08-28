"""
https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_good_subarray_splits(self, nums: list[int]) -> int:
        """
        number of good subarray splits
        """
        cnt = 0
        l = 0
        m = 10 ** 9 + 7
        for r, x in enumerate(nums):
            if x == 1:
                if cnt == 0:
                    cnt = 1
                else:
                    cnt *= (r - l + 1)
                    cnt %= m

                l = r + 1

        return cnt % m
