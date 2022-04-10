"""
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
"""


from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """
        1. If could make one row the same, then all the numbers in the target
            row will either be A[0] or B[0].
        2. Try to make one row as A[0] or B[0] and choose the minimum rotates.
        """
        def check(t: int) -> int:
            ra, rb, notFound = 0, 0, False
            for a, b in zip(A, B):
                if a == t or b == t:
                    if a != t:
                        ra += 1

                    if b != t:
                        rb += 1
                else:
                    notFound = True
                    break

            if notFound:
                return -1
            else:
                return min(ra, rb)

        if len(A) != len(B):
            return -1

        # Make the whole row as A[0].
        rslt = check(A[0])
        if rslt < 0:
            return check(B[0])
        else:
            return rslt


print(Solution().minDominoRotations(
    [1, 2, 1, 1, 1, 2, 2, 2],
    [2, 1, 2, 2, 2, 2, 2, 2]))
