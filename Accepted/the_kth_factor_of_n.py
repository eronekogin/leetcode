"""
https://leetcode.com/problems/the-kth-factor-of-n/
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        remainCnt = k
        for factor in range(1, int(n ** 0.5) + 1):
            if n % factor == 0:
                factors.append(factor)
                remainCnt -= 1

            if remainCnt == 0:
                return factor

        if factors[-1] ** 2 == n:
            factors.pop()

        if remainCnt > len(factors):  # Not enough factors.
            return -1

        return n // factors[-remainCnt]
