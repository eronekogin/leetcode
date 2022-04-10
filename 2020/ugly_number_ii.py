"""
https://leetcode.com/problems/ugly-number-ii/
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Suppose we have an array k of first n ugly numbers, we only know the
        first one k[0] = 1. Then we have:

            k[1] = min(k[0] * 2, k[0] * 3, k[0] * 5) = k[0] * 2 = 2

        So we increase the pointer to prime 2 and then we test:

            k[2] = min(k[1] * 2, k[0] * 3, k[0] * 5) = k[0] * 3 = 3

        Then we test:

            k[3] = min(k[1] * 2, k[1] * 3, k[0] * 5) = k[1] * 2 = 4
            k[4] = min(k[2] * 2, k[1] * 3, k[0] * 5) = k[0] * 5 = 5
            k[5] = min(k[2] * 2, k[1] * 3, k[1] * 5) = k[2] * 2 or k[1] * 3

        So for k[5], both pointers to prime 2 and 3 needs to be increased.
        """
        if n < 1:
            return 0

        k = [1] * n
        i2 = i3 = i5 = 0
        p2, p3, p5 = 2, 3, 5
        for i in range(1, n):
            k[i] = min(p2, p3, p5)
            if k[i] == p2:
                i2 += 1
                p2 = k[i2] * 2

            if k[i] == p3:
                i3 += 1
                p3 = k[i3] * 3

            if k[i] == p5:
                i5 += 1
                p5 = k[i5] * 5

        return k[-1]
