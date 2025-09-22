"""
https://leetcode.com/problems/minimum-index-of-a-valid-split/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def minimum_index(self, nums: list[int]) -> int:
        """
        minimum index
        """
        left = Counter()
        right = Counter(nums)

        for i, x in enumerate(nums):
            left[x] += 1
            right[x] -= 1

            if left[x] * 2 > i + 1 and right[x] * 2 > len(nums) - i - 1:
                return i

        return -1
