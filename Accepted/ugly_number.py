"""
https://leetcode.com/problems/ugly-number/
"""


class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        currNum = num
        for p in (2, 3, 5):
            while not currNum % p:
                currNum //= p

        return currNum == 1
