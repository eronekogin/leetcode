"""
https://leetcode.com/problems/rotate-array/
"""


from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Suppose nums = [1, 2, 3, 4, 5], k = 2

        1. Reverse the full list -> [5, 4, 3, 2, 1]
        2. Reverse the first 2 items -> [4, 5, 3, 2, 1]
        3. Reverse the remaining items -> [4, 5, 1, 2, 3]
        """
        n = len(nums)
        cut = k % n
        self.reverse(nums, 0, n - 1)  # Reverse the whole input list first.
        self.reverse(nums, 0, cut - 1)  # Then reverse the first k items.
        self.reverse(nums, cut, n - 1)  # Then reverse the remaining n-k items.

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
