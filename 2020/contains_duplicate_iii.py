"""
https://leetcode.com/problems/contains-duplicate-iii/
"""


from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
            self, nums: List[int], k: int, t: int) -> bool:
        """
        Use the same idea as bucket sort. Suppose we have k
        buckets with each one's depth as t + 1, then if there are
        two numbers with difference <= t, there could only be two cases:

        1. Those two numbers are in the same bucket.
        2. Those two numbers are in the neighbour buckets.
        """
        if k < 0 or t < 0:  # Absolute difference should always be positive.
            return False

        buckets, depth = {}, t + 1
        for i, num in enumerate(nums):
            # Calculate which bucket the current number belongs to.
            b = num // depth
            for bucket in (b - 1, b, b + 1):
                if bucket in buckets and abs(buckets[bucket] - num) < depth:
                    return True

            buckets[b] = num  # Update the bucket with the latest number.
            if i >= k:  # If there are more than k buckets, delete the first.
                del buckets[nums[i - k] // depth]

        return False
