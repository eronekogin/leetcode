"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
"""


from typing import List

from heapq import heappush, heappop, heapify


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        1. Find the initial range which is identified by comparing all the
            first element in the given lists.
        2. Our task is to reduce the initial range to a smaller one. Notice
            that we cannot decrease the current maximum value as it serves as
            the minimum value from one of the given list (all the lists are
            in non-descending order), so we could only try to increase the
            current minimum value by checking the next number in the target
            list where the current minimum value is on.
        3. When one of the list is exhahusted, we don't need to process
            further to avoid exclusion of a given list.
        """
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        start, end = float('-inf'), float('inf')
        right = max(heap)[0]
        heapify(heap)  # Make the target list to a heap.
        while heap:
            left, r, c = heappop(heap)
            if right - left < end - start:
                start, end = left, right

            c += 1  # Check the next number in the current min list.
            if c == len(nums[r]):  # The given list is exhausted.
                return [start, end]

            v = nums[r][c]
            right = max(right, v)  # Find the next maximum value.
            heappush(heap, (v, r, c))


print(Solution().smallestRange(
    [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
