"""
https://leetcode.com/problems/maximum-good-subarray-sum/description/
"""

from collections import defaultdict
from math import inf


class Solution:
    """
    Solution
    """

    def maximum_subarray_sum(self, nums: list[int], k: int) -> int:
        """
        maximum subarray sum
        """
        min_prev_sums = defaultdict(lambda: inf)
        curr_sum = 0
        max_sum = -inf

        for x in nums:
            min_prev_sums[x] = min(min_prev_sums[x], curr_sum)
            curr_sum += x
            max_sum = max(
                max_sum,
                curr_sum - min_prev_sums[x - k],
                curr_sum - min_prev_sums[x + k]
            )

        if max_sum > -inf:
            return int(max_sum)

        return 0  # No subarray found


print(Solution().maximum_subarray_sum([4, 7, 3, 5, 5], 2))
