"""
https://leetcode.com/problems/my-calendar-ii/
"""


class BSTNode:

    def __init__(self, start: int, end: int):
        self.left = self.right = None
        self.start = start
        self.end = end
        self.isDoubleBooked = False


class MyCalendarTwo:

    def __init__(self):
        self._root = None

    def book(self, start: int, end: int) -> bool:
        if not self._root:
            self._root = BSTNode(start, end)
            return True

        if self._insertable(start, end):
            self._insert(start, end)
            return True

        return False

    def _insertable(self, start: int, end: int) -> bool:
        def _do(s: int, e: int, currNode: BSTNode) -> bool:
            if s >= e:  # Empty interval.
                return True

            if not currNode:  # No existing node.
                return True

            if s >= currNode.end:  # Check right sub tree.
                return _do(s, e, currNode.right)
            elif e <= currNode.start:  # Check left sub tree.
                return _do(s, e, currNode.left)
            elif currNode.isDoubleBooked:
                return False  # No tripple overlap is allowed.
            else:  # Overlap discovered.
                if s >= currNode.start and e <= currNode.end:
                    return True  # New interval is inside the existing one.
                else:  # Check left and right.
                    return _do(s, currNode.start, currNode.left) \
                        and _do(currNode.end, e, currNode.right)

        return _do(start, end, self._root)

    def _insert(self, start: int, end: int) -> None:
        def _do(s: int, e: int, currNode: BSTNode) -> BSTNode:
            if s >= e:  # Empty interval.
                return currNode

            if not currNode:
                return BSTNode(s, e)

            if s >= currNode.end:  # Check right sub tree.
                currNode.right = _do(s, e, currNode.right)
            elif e <= currNode.start:  # Check left sub tree.
                currNode.left = _do(s, e, currNode.left)
            else:
                currNode.isDoubleBooked = True
                leftStart = min(currNode.start, s)
                currNode.start = max(currNode.start, s)
                rightEnd = max(currNode.end, e)
                currNode.end = min(currNode.end, e)
                currNode.left = _do(
                    leftStart, currNode.start, currNode.left)
                currNode.right = _do(
                    currNode.end, rightEnd, currNode.right)

            return currNode

        _do(start, end, self._root)


m = MyCalendarTwo()
for start, end in [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]:
    m.book(start, end)
