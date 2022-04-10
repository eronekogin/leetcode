"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""


from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        risingStart = risingEnd = None

        # Scan the list from left to right until the slop begins to fall, then
        # find the minimum value from that point until the end of the list.
        for i in range(n - 1):
            if nums[i + 1] < nums[i]:
                risingEnd = i
                break

        if risingEnd is None:  # Already in ascending order.
            return 0

        minNum = min(nums[risingEnd + 1:])

        # Scan the list from right to left until the slop begins to rise, then
        # find the maximum value from that point until the start of the list.
        for i in range(n - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                risingStart = i
                break

        if risingStart is None:  # Already in descending order.
            return n

        maxNum = max(nums[:risingStart])

        # Find the correct positions for the above min and max numbers.
        for i in range(n):
            if minNum < nums[i]:
                start = i
                break

        for i in range(n - 1, -1, -1):
            if maxNum > nums[i]:
                end = i
                break

        return end - start + 1

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        """
        Sort the list and compare the difference.
        """
        rslt = [
            i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]

        if not rslt:
            return 0

        return rslt[-1] - rslt[0] + 1


print(Solution().findUnsortedSubarray([1, 3, 2, 4, 5]))
