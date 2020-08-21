"""
https://leetcode.com/problems/sort-array-by-parity/
"""


from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        One pass without extra space.
        """
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] & 1 == 1:
                while r > l and A[r] & 1 == 1:
                    r -= 1

                A[l], A[r] = A[r], A[l]
                r -= 1

            l += 1

        return A

    def sortArrayByParity2(self, A: List[int]) -> List[int]:
        """
        One pass with O(n) extra space.
        """
        evens, odds = [], []
        for num in A:
            if num & 1 == 1:
                odds.append(num)
            else:
                evens.append(num)

        return evens + odds
