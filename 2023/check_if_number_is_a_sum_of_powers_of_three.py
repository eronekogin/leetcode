"""
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            n, r = divmod(n, 3)
            if r == 2:
                return False

        return True
