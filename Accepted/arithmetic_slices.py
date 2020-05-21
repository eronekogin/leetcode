"""
https://leetcode.com/problems/arithmetic-slices/
"""


from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A or len(A) < 3:
            return 0

        total = cnt = 0
        for i in range(2, len(A)):
            if A[i] + A[i - 2] == A[i - 1] << 1:  # A[I]-A[I-1]==A[I-1]-A[I-2].
                cnt += 1
                total += cnt
            else:
                cnt = 0

        return total


print(Solution().numberOfArithmeticSlices([1, 2, 3, 4]))
