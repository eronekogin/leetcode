"""
https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
"""


from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        1. First calculate the minimum numbers from index i to the end of the
            given list by scanning the list from right to left.
        2. Then for a given list, suppose at index k, the maximum of the
            previous numbers is less or equal than the minimum of the next
            numbers, then we could divide this list into two chunks at index k,
            so that the first chunk contains the number at index k and the
            second chunk contains the remaining numbers.
        """
        N = len(arr)
        minNums = [None] * N
        minNums[-1] = arr[-1]
        for i in range(N - 2, -1, -1):
            minNums[i] = min(arr[i], minNums[i + 1])

        chunks, maxNum = 1, arr[0]
        for i in range(N - 1):
            if maxNum <= minNums[i + 1]:
                chunks += 1

            maxNum = max(maxNum, arr[i + 1])

        return chunks
