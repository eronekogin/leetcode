"""
https://leetcode.com/problems/sum-of-square-numbers/
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c ** 0.5) + 1):
            sb = (c - a ** 2) ** 0.5
            if int(sb) == sb:
                return True

        return False
