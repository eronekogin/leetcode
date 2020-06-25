"""
https://leetcode.com/problems/sort-characters-by-frequency/
"""


from collections import Counter
from heapq import heappush, heappop


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Use heap sort.
        """
        cnt, heap, rslt = Counter(s), [], []
        for c, freq in cnt.items():
            heappush(heap, (-freq, c))

        while heap:
            freq, c = heappop(heap)
            rslt += [c] * (-freq)

        return ''.join(rslt)

    def frequencySort2(self, s: str) -> str:
        """
        Pure python function.
        """
        return ''.join(c * f for c, f in Counter(s).most_common())

    def frequencySort3(self, s: str) -> str:
        """
        Use built-in sort, which is timsort.
        """
        return ''.join(c * f for c, f in sorted(
            Counter(s).items(), key=lambda x: x[1], reverse=True))
