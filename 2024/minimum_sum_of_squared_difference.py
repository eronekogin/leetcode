"""
https://leetcode.com/problems/minimum-sum-of-squared-difference/description/
"""


from heapq import heapify, heappop, heappush


class Solution:
    """
    Solution
    """

    def min_sum_square_diff(
            self,
            nums1: list[int],
            nums2: list[int],
            k1: int,
            k2: int
    ) -> int:
        """
        min sum square diff
        """
        heap = [-abs(a - b) for a, b in zip(nums1, nums2)]
        remain = k1 + k2

        if sum(heap) + k1 + k2 >= 0:
            return 0

        n = len(nums1)
        heapify(heap)
        while heap and remain > 0:
            curr = heappop(heap)
            gap = max(remain // n, 1)
            if curr + gap < 0:
                heappush(heap, curr + gap)

            remain -= gap

        return sum(x * x for x in heap)


print(Solution().min_sum_square_diff([1, 4, 10, 12], [5, 8, 6, 9], 1, 1))
