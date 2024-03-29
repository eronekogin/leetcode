"""
https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_top(self, nums: list[int], k: int) -> int:
        """
        maximum top
        """
        n = len(nums)

        if k == 0:
            return nums[0]

        if k == 1:
            if n == 1:  # Empty pile
                return -1

            return nums[1]

        if n == 1:
            if k & 1:  # Empty pile
                return -1

            return nums[0]

        max_end = min(k - 1, n)

        if k < n:
            # delete all vs keep last
            return max(nums[:max_end] + [nums[k]])

        return max(nums[:max_end])
