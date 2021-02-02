"""
https://leetcode.com/problems/max-chunks-to-make-sorted/
"""


from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Keep monitoring the current maximum number for the first k numbers.
        Then if at the index k the maximum number equals to k, it means the
        previous k numbers are from 0 to k - 1, which could be cut as a chunk.

        The above is based on the fact that the given list is a permutation of
        0 to N - 1, where each number occurs once. 
        """
        maxNum, chunks = 0, 0
        for i, num in enumerate(arr):
            maxNum = max(maxNum, num)
            if maxNum == i:
                chunks += 1

        return chunks


print(Solution().maxChunksToSorted([2, 0, 1]))
