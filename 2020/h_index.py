"""
https://leetcode.com/problems/h-index/
"""


from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Take the idea of bucket sort algorithm.
        """
        n = len(citations)
        buckets = [0] * (n + 1)
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        cnt = 0
        for i in range(n, -1, -1):
            cnt += buckets[i]
            if cnt >= i:
                return i

        return 0
