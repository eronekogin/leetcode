"""
https://leetcode.com/problems/data-stream-as-disjoint-intervals/
"""


from typing import List


class SummaryRanges:

    def __init__(self):
        self.startWith = {}  # start: end
        self.endWith = {}  # end: start
        self.visited = set()

    def addNum(self, val: int) -> None:
        if val in self.visited:
            return

        self.visited.add(val)

        # Check if any existing interval starts with val + 1.
        end = self.startWith.pop(val + 1, val)

        # Check if any existing interval ends with val - 1.
        start = self.endWith.pop(val - 1, val)

        # Add the new interval back to the memo dictionaries.
        self.startWith[start] = end
        self.endWith[end] = start

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.startWith.items())
