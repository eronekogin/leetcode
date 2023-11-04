"""
https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/
"""


from itertools import accumulate
from collections import Counter


class Solution:
    """
    Solution
    """

    def ways_to_partition(self, nums: list[int], k: int) -> int:
        """
        ways_to_partition
        """
        prefix_sum = list(accumulate(nums))
        total = prefix_sum[-1]
        prev_half = Counter()
        next_half = Counter(prefix_sum)

        next_half[total] -= 1  # Last prefix sum is never used.

        max_pivots = 0
        if total & 1 == 0:  # Even sum
            max_pivots = next_half[total >> 1]

        # Try to change any num at index i to k.
        n = len(nums)
        for i, v in enumerate(nums):
            curr_pivots = 0

            if v != k:
                new_total = total + k - v
                if new_total & 1 == 0:  # New total is even sum.
                    half_sum = new_total >> 1
                    if i > 0:
                        curr_pivots += prev_half[half_sum]

                    if i + 1 < n:
                        curr_pivots += next_half[half_sum + v - k]

                max_pivots = max(max_pivots, curr_pivots)

            prev_half[prefix_sum[i]] += 1
            next_half[prefix_sum[i]] -= 1

        return max_pivots


print(Solution().ways_to_partition([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 30827, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
