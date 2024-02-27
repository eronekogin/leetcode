"""
https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/description/
"""


from heapq import heappushpop, heapify


class Solution:
    """
    Solution
    """

    def minimum_difference(self, nums: list[int]) -> int:
        """
        minimum difference
        """
        n = len(nums) // 3

        # Get left
        left = [-x for x in nums[:n]]
        heapify(left)
        sum_left = [-sum(left)]

        for i in range(n, n << 1):
            curr = heappushpop(left, -nums[i])
            sum_left.append(sum_left[-1] + curr + nums[i])

        # Get right
        right = nums[n << 1:]
        heapify(right)
        sum_right = [sum(right)]

        for i in reversed(range(n, n << 1)):
            curr = heappushpop(right, nums[i])
            sum_right.append(sum_right[-1] - curr + nums[i])

        return min(l - r for l, r in zip(sum_left, sum_right[::-1]))
