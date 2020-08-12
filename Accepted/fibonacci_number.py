"""
https://leetcode.com/problems/fibonacci-number/
"""


class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for _ in range(1, N + 1):
            a, b = b, a + b

        return a
