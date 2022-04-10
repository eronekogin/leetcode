"""
https://leetcode.com/problems/maximum-gap/
"""


from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:  # The input list contains less than 2 elements.
            return 0

        minNum, maxNum = min(nums), max(nums)
        bucketSize = max(1, (maxNum - minNum) // (n - 1))
        buckets = [
            [None, None] for _ in range((maxNum - minNum) // bucketSize + 1)]

        # Distribute the numbers in nums to the target buckets.
        for num in nums:
            bucket = buckets[(num - minNum) // bucketSize]
            bucket[0] = num if bucket[0] is None else min(num, bucket[0])
            bucket[1] = num if bucket[1] is None else max(num, bucket[1])

        # Calculate maximum gap between adjancent bucket.
        pre, maxGap = None, 0
        for bucket in buckets:
            if bucket[0] is not None:
                if pre is not None:
                    maxGap = max(maxGap, bucket[0] - pre)

                pre = bucket[1]

        return maxGap
