"""
https://leetcode.com/problems/binary-number-with-alternating-bits/
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        currNum, currBit = n >> 1, n & 1
        while currNum:
            nextBit = currNum & 1
            if nextBit != currBit:
                currBit = nextBit
                currNum >>= 1
            else:
                return False

        return True


print(Solution().hasAlternatingBits(5))
