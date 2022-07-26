"""
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
"""


class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return True

        sortedArr = sorted(arr)
        for end in range(2, len(sortedArr)):
            if sortedArr[end] + sortedArr[end - 2] != (sortedArr[end - 1] << 1):
                return False

        return True
