"""
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
"""


class Solution:
    def maxNonOverlapping(self, nums: list[int], target: int) -> int:
        seen = {0}  # 0 is seen initially.
        prefixSum = 0
        cnt = 0
        for num in nums:
            prefixSum += num
            if prefixSum - target in seen:
                cnt += 1
                seen = set()

            seen.add(prefixSum)

        return cnt
