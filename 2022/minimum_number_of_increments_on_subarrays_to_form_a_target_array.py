"""
https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
"""


class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        """
        Think of one operation is to add one row to the bottom of the bricks
        until we cannot add more.
        """
        cnt = target[0]
        for i in range(1, len(target)):
            cnt += max(0, target[i] - target[i - 1])

        return cnt
