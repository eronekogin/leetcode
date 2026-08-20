"""
https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int]) -> int:
        """
        min operations
        """
        is_flipped = 0
        cnt = 0

        for x in nums:
            if x ^ is_flipped == 0:
                cnt += 1
                is_flipped ^= 1

        return cnt
