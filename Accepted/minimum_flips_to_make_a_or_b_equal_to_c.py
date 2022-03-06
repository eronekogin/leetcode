"""
https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flipCnt = 0
        while a or b or c:
            if c & 1 == 1:
                if a & 1 == 0 and b & 1 == 0:  # Only flip when both zero.
                    flipCnt += 1
            else:
                if a & 1 == 1:
                    flipCnt += 1

                if b & 1 == 1:
                    flipCnt += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flipCnt


print(Solution().minFlips(8, 3, 5))
