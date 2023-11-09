"""
https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
"""


class Solution:
    """
    Solution
    """

    def min_operations(self, grid: list[list[int]], x: int) -> int:
        """
        min_operations
        """
        nums = sorted(x for row in grid for x in row)
        target = nums[len(nums) >> 1]

        cnt = 0
        for num in nums:
            q, r = divmod(abs(num - target), x)
            if r > 0:
                return -1

            cnt += q

        return cnt
