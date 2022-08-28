"""
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        isFlipped = 0
        currLen = (1 << n) - 1
        remainOffset = k
        while remainOffset > 1:
            if remainOffset == (currLen >> 1) + 1:
                return str(1 ^ isFlipped)

            if remainOffset > (currLen >> 1) + 1:
                # offset is on the right part.
                remainOffset = currLen + 1 - remainOffset
                isFlipped = 1 - isFlipped

            currLen >>= 1

        return str(isFlipped)
