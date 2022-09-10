"""
https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
"""


class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            if arr[i: i + m * k] == arr[i: i + m] * k:
                return True

        return False
