"""
https://leetcode.com/problems/my-calendar-iii/
"""


class BSTNode:

    def __init__(self, start: int, end: int, overlaps: int):
        self.start, self.end = start, end
        self.left = self.right = None
        self.overlaps = overlaps

    def __repr__(self) -> str:
        return '({0}, {1}, {2})'.format(self.start, self.end, self.overlaps)


class MyCalendarThree:

    def __init__(self):
        self._root = None
        self._maxOverlaps = None

    def book(self, start: int, end: int) -> int:
        if not self._root:
            self._root = BSTNode(start, end, 1)
            self._maxOverlaps = 1
        else:
            self._insert(start, end)

        return self._maxOverlaps

    def _insert(self, start: int, end: int) -> None:
        def _do(s: int, e: int, overlaps: int, currNode: BSTNode) -> None:
            if not currNode:  # Create a new node.
                self._maxOverlaps = max(self._maxOverlaps, overlaps)
                return BSTNode(s, e, overlaps)

            if s >= currNode.end:  # Check right.
                currNode.right = _do(s, e, overlaps, currNode.right)
            elif e <= currNode.start:  # Check left.
                currNode.left = _do(s, e, overlaps, currNode.left)
            else:  # Found new overlap.
                sMin, sMax = min(s, currNode.start), max(s, currNode.start)
                eMin, eMax = min(e, currNode.end), max(e, currNode.end)
                if sMin < sMax:
                    if s < currNode.start:
                        currNode.left = _do(
                            sMin, sMax, overlaps, currNode.left)
                    else:
                        currNode.left = _do(
                            sMin, sMax, currNode.overlaps, currNode.left)

                if eMin < eMax:
                    if e < currNode.end:
                        currNode.right = _do(
                            eMin, eMax, currNode.overlaps, currNode.right)
                    else:
                        currNode.right = _do(
                            eMin, eMax, overlaps, currNode.right)

                currNode.start, currNode.end = sMax, eMin
                currNode.overlaps += overlaps
                self._maxOverlaps = max(self._maxOverlaps, currNode.overlaps)

            return currNode

        _do(start, end, 1, self._root)


events = [
    [97, 100], [51, 65], [27, 46], [90, 100], [20, 32], [15, 28], [60, 73],
    [77, 91], [67, 85], [58, 72], [74, 93], [73, 83], [71, 87], [97, 100],
    [14, 31], [26, 37], [66, 76], [52, 67], [24, 43], [6, 23], [94, 100],
    [33, 44], [30, 46], [6, 20], [71, 87], [49, 59], [38, 55], [4, 17],
    [46, 61], [13, 31], [94, 100], [47, 65], [9, 25], [4, 20], [2, 17],
    [28, 42], [26, 38], [72, 83], [43, 61], [18, 35]]

m = MyCalendarThree()
print([m.book(*e) for e in events])
