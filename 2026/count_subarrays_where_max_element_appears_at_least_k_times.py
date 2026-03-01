"""
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
"""


class Solution:
    """
    Solution
    """

    def count_subarrays(self, nums: list[int], k: int) -> int:
        """
        count subarrays
        """
        max_num = max(nums)
        pivots: list[int] = []
        cnt = 0
        for i, x in enumerate(nums):
            if x == max_num:
                pivots.append(i)

            if len(pivots) >= k:
                # The number of possible starting positions
                # of subarrays that ends at index i with
                # max number occurred at least k times is
                # pivots[-k] + 1
                cnt += pivots[-k] + 1

        return cnt
