"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/description/
"""


class Solution:
    """
    Solutiuon
    """

    def make_similar(self, nums: list[int], target: list[int]) -> int:
        """
        make similar
        """
        sorted_nums = sorted(nums, key=lambda x: (x & 1, x))
        sorted_target = sorted(target, key=lambda x: (x & 1, x))

        return sum(abs(a - b) for a, b in zip(sorted_nums, sorted_target)) // 4
