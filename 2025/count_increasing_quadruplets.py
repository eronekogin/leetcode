"""
https://leetcode.com/problems/count-increasing-quadruplets/description/
"""


class Solution:
    """
    Soluton
    """

    def count_quadruplets(self, nums: list[int]) -> int:
        """
        count quadruplets
        """
        n = len(nums)
        cnt = [0] * n  # Triplets consisted with (i, j, k)
        rslt = 0
        for l in range(n):
            prev_small = 0

            for j in range(l):
                if nums[l] > nums[j]:
                    prev_small += 1

                    # For any new nums[j] < nums[l], l can
                    # help form the new quadruplets with any
                    # triplets indexed at j.
                    rslt += cnt[j]
                elif nums[l] < nums[j]:
                    # prev_small stores any previous numbers
                    # smaller than nums[l], which could help
                    # form triplets (?, j, l)
                    cnt[j] += prev_small

        return rslt
