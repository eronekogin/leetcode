"""
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
"""


class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def count_digits(num: int) -> int:
            cnt = 0
            while num:
                cnt += 1
                num &= num - 1  # Unset the rightmost valid bit to zero.

            return cnt

        return sorted(arr, key=lambda x: (count_digits(x), x))
