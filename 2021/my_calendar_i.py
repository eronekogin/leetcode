"""
https://leetcode.com/problems/my-calendar-i/
"""


class MyCalendar:

    def __init__(self):
        self._intervals = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self._intervals:
            if not (end <= s or start >= e):
                return False

        self._intervals.append((start, end))
        return True


class BSTNode:

    def __init__(self, start: int, end: int):
        self.s = start
        self.e = end
        self.left = self.right = None

    def insert(self, start: int, end: int) -> bool:
        if self.s >= end:
            if not self.left:
                self.left = BSTNode(start, end)
                return True
            else:
                return self.left.insert(start, end)
        elif self.e <= start:
            if not self.right:
                self.right = BSTNode(start, end)
                return True
            else:
                return self.right.insert(start, end)
        else:
            return False


class MyCalendar2:
    """
    Use BST instead of a single list to accelarate the searching speed.
    """

    def __init__(self):
        self._root = None

    def book(self, start: int, end: int) -> bool:
        if not self._root:
            self._root = BSTNode(start, end)
            return True
        else:
            return self._root.insert(start, end)
