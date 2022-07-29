"""
https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/
"""


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        if k >= ((n * (n - 1)) >> 1):
            return ''.join(sorted(num))

        for digit in range(10):
            i = num.find(str(digit))
            if 0 <= i <= k:
                return num[i] + self.minInteger(num[:i] + num[i + 1:], k - i)
