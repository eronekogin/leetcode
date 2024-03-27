"""
https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def find_k_distant_indices(self, nums: list[int], key: int, k: int) -> list[int]:
        """
        find_k_distant_indices
        """
        rslt: list[int] = []
        pivots = [i for i, x in enumerate(nums) if x == key]
        prev = 0
        for p in pivots:
            start = max(prev, p - k)
            end = min(p + k, len(nums) - 1)
            rslt.extend(range(start, end + 1))
            prev = end + 1

        return rslt
