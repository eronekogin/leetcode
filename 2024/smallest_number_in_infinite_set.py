"""
https://leetcode.com/problems/smallest-number-in-infinite-set/description/
"""


from heapq import heappop, heappush


class SmallestInfiniteSet:
    """
    Smallest infinite set
    """

    def __init__(self):
        self.smallest = 1
        self.new_smallests = []

    def pop_smallest(self) -> int:
        """
        pop smallest
        """
        if self.new_smallests:
            return heappop(self.new_smallests)

        self.smallest += 1
        return self.smallest - 1

    def add_back(self, num: int) -> None:
        """
        add back
        """
        if num < self.smallest and num not in set(self.new_smallests):
            heappush(self.new_smallests, num)
