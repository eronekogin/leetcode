"""
https://leetcode.com/problems/sequentially-ordinal-rank-tracker/
"""


from heapq import heappush, heappop


class MinHeapItem:
    """
    MinHeapItem
    """

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score or \
            (self.score == other.score and self.name > other.name)


class MaxHeapItem:
    """
    MaxHeapItem
    """

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score > other.score or \
            (self.score == other.score and self.name < other.name)


class SORTracker:
    """
    SORTracker
    """

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.k = 0

    def add(self, name: str, score: int) -> None:
        """
        add scenic localtion
        """
        heappush(self.min_heap, MinHeapItem(name, score))
        if len(self.min_heap) > self.k + 1:
            temp = heappop(self.min_heap)
            heappush(self.max_heap, MaxHeapItem(temp.name, temp.score))

    def get(self) -> str:
        """
        get best scenic location
        """
        ans = self.min_heap[0].name
        self.k += 1
        if self.max_heap:
            temp = heappop(self.max_heap)
            heappush(self.min_heap, MinHeapItem(temp.name, temp.score))
        return ans
