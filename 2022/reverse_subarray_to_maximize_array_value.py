"""
https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/
"""


class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        """
        See https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/discuss/489882/O(n)-Solution-with-explanation for more details.
        """
        minAB, maxCD, totalSum = float('inf'), float('-inf'), 0
        for a, b in zip(nums, nums[1:]):
            totalSum += abs(a - b)
            maxCD = max(min(a, b), maxCD)
            minAB = min(max(a, b), minAB)

        # Calculate change after reverse from minAB to maxCD
        delta = max(0, (maxCD - minAB) << 1)

        # Checking boundaries.
        for a, b in zip(nums, nums[1:]):
            low = -abs(a - b) + abs(nums[0] - b)
            high = -abs(a - b) + abs(nums[-1] - a)
            delta = max(low, high, delta)

        return totalSum + delta
