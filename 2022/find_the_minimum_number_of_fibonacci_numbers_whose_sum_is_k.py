"""
https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
"""


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        """
        Always find the fibonacci number that is closest to k, then recursively
        calculate the result until no more could be reduced.
        """
        if k < 2:
            return k

        a = b = 1
        while b <= k:
            a, b = b, a + b

        if b > k:
            return 1 + self.findMinFibonacciNumbers(k - a)
