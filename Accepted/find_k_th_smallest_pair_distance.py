"""
https://leetcode.com/problems/find-k-th-smallest-pair-distance/
"""


from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        1. Find the kth smallest distance is to find the distance where there
            are exactly k pairs whose distance is <= the target distance.
        2. We sort the input list first and then use a sliding window to 
            count the pairs that are less than the target.
        3. Then we use binary search to search in the difference. Since we
            have already sorted the input list, the maximum distance is
            given by pair (nums[0], nums[-1]).
        """
        def is_enough(diff: int) -> bool:
            """
            Check if there are at least k pairs whose distance is less than
            the given diff.
            """
            cnt, left = 0, 0
            for right, num in enumerate(nums):
                while num - nums[left] > diff:
                    left += 1

                cnt += right - left

            return cnt >= k

        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = low + ((high - low) >> 1)
            if is_enough(mid):
                high = mid
            else:
                low = mid + 1

        return low
