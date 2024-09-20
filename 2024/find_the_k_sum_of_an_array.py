"""
https://leetcode.com/problems/find-the-k-sum-of-an-array/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def k_sum(self, nums: list[int], k: int) -> int:
        """
        For any number in nums, we can just consider its absolute value since
        for positive numbers, reduce it from the current max sum will give us
        the next max sum while for negative numbers, add it to the current max
        sum will also give us the next max sum.

        In order to generate the next max sum, we subtract the current max sum
        with the number that has the smallest absolute value. Besides, we should
        also generate an extra candidate by ignore the previous used absolute
        value. So we need two pushes to the queue in each loop.
        """
        max_sum = sum([x for x in nums if x > 0] or [0])
        abs_nums = sorted(map(abs, nums))
        heap: list[tuple[int, int]] = [(-max_sum + abs_nums[0], 0)]
        next_sum = -max_sum

        for _ in range(k - 1):
            next_sum, i = heappop(heap)
            if i + 1 < len(abs_nums):
                heappush(
                    heap,
                    (next_sum - abs_nums[i] + abs_nums[i + 1], i + 1)
                )

                heappush(
                    heap,
                    (next_sum + abs_nums[i + 1], i + 1)
                )

        return -next_sum
