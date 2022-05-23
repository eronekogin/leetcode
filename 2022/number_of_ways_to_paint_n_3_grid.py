"""
https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
"""


class Solution:
    def numOfWays(self, n: int) -> int:
        """
        Consider the state of the first row:
            Pattern#121: 121, 131, 212, 232, 313, 323
            Pattern#123: 123, 132, 213, 231, 312, 321

        Then for each pattern, it can be followed with:
            Pattern#121: 212, 213, 232, 312, 313
            Pattern#123: 212, 231, 312, 232

        So we have:
            b121 = 3 * a121 + 2 * a123
            b123 = 2 * a121 + 2 * a123
        """
        a121 = a123 = 6
        for _ in range(n - 1):
            a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2

        return (a121 + a123) % (10 ** 9 + 7)
