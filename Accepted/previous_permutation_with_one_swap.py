"""
https://leetcode.com/problems/previous-permutation-with-one-swap/
"""


class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        i = len(arr) - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1

        if i == -1:  # arr is already sorted in ascending order.
            return arr  # No swap could be made.

        # Then try to find the largest number on the right of index i which
        # is less than arr[i].
        maxIdx, maxLimit = i + 1, arr[i]
        for currIdx in range(i + 2, len(arr)):
            if arr[currIdx] < maxLimit and arr[currIdx] > arr[maxIdx]:
                maxIdx = currIdx

        # Make one swap.
        arr[maxIdx], arr[i] = arr[i], arr[maxIdx]

        return arr


print(Solution().prevPermOpt1([3, 1, 1, 3]))
