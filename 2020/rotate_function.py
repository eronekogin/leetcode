"""
https://leetcode.com/problems/rotate-function/
"""


from typing import List


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        """
        1. BK[i] = BK-1[i - 1]  # Clockwise rotate.
        2. FK[I] = 0*BK[0] + 1*BK[1] + ... + (N-1)BK[N]
           FK-1[I] = 0*BK-1[0] + 1*BK-1[1] + ... + 
               (N-2)*BK-1[N-1] + (N-1)*BK-1[N] = 
               0*BK[1] + 1*BK[2] + ... + (N-2)*BK[N] + (N-1)*BK[0]
           So FK[I] - FK-1[I] = BK[1] + ... + BK[N] + (1-N)*BK[0]
              = (BK[0] + ... + BK[N]) - N*BK[0]

           So FK[I] = FK-1[I] + SUM(A) - N*BK[0].
        3. BK[0] = A[-K]
        """
        if not A:
            return 0

        n = len(A)
        if n == 1:
            return 0

        fk = sumA = 0
        for i, num in enumerate(A):
            sumA += num
            fk += i * num

        rslt = fk
        for i in range(1, n):
            fk += sumA - n * A[-i]
            rslt = max(rslt, fk)

        return rslt


print(Solution().maxRotateFunction([4, 3, 2, 6]))
