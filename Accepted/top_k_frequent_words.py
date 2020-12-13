"""
https://leetcode.com/problems/top-k-frequent-words/
"""


from heapq import heapify, heappop
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = Counter(words)
        heap = [(-freq, w) for w, freq in freqs.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]
