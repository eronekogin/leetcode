"""
https://leetcode.com/problems/design-a-number-container-system/description/
"""

from collections import defaultdict
from heapq import heappop, heappush


class NumberContainers:
    """
    Number containers
    """

    def __init__(self):
        self.index_to_number: dict[int, int] = {}
        self.nums_to_indexes_set: defaultdict[int, set[int]] = defaultdict(set)
        self.nums_to_indexes_heap: defaultdict[int, list[int]] = defaultdict(
            list)

    def change(self, index: int, number: int) -> None:
        """
        change
        """
        if index not in self.index_to_number:
            self.index_to_number[index] = number
            self.nums_to_indexes_set[number].add(index)
            heappush(self.nums_to_indexes_heap[number], index)
            return

        prev_num = self.index_to_number[index]
        if number != prev_num:
            self.nums_to_indexes_set[prev_num].remove(index)
            self.index_to_number[index] = number
            self.nums_to_indexes_set[number].add(index)
            heappush(self.nums_to_indexes_heap[number], index)

    def find(self, number: int) -> int:
        """
        find
        """
        curr_indexes = self.nums_to_indexes_set[number]
        curr_heap = self.nums_to_indexes_heap[number]
        while curr_heap and curr_heap[0] not in curr_indexes:
            heappop(curr_heap)

        if not curr_heap:
            return -1

        return curr_heap[0]


nc = NumberContainers()
nc.find(10)
nc.change(2, 10)
nc.change(1, 10)
nc.change(3, 10)
nc.change(5, 10)
nc.find(10)
nc.change(1, 20)
nc.find(10)
