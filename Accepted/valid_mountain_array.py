"""
https://leetcode.com/problems/valid-mountain-array/
"""


from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, n = 1, len(arr)
        if n < 3:
            return False

        while i < n and arr[i] > arr[i - 1]:
            i += 1

        if i == 1 or i == n:  # All dereasing or increasing.
            return False

        while i < n and arr[i] < arr[i - 1]:
            i += 1

        return i == n  # Fall to the end from the peak.
