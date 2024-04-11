"""
https://leetcode.com/problems/minimum-operations-to-halve-array-sum/description/
"""


from heapq import heappush, heappop, heapify


class Solution:
    """
    Solution
    """

    def halve_array(self, nums: list[int]) -> int:
        """
        halve array
        """
        ops = 0
        heap = [-float(x) for x in nums]
        heapify(heap)
        curr_sum = sum(nums)
        target = curr_sum / 2
        while curr_sum > target:
            x = heappop(heap)
            half = x / 2
            curr_sum += half
            ops += 1
            heappush(heap, half)

        return ops


print(Solution().halve_array(
    [18, 22, 62, 61, 1, 88, 17, 98, 38, 32, 51, 57, 7, 29, 40, 61, 62, 13, 89, 41, 73, 85, 88, 60, 59, 76, 71, 76, 76, 41, 29, 43, 19, 9, 79]))
