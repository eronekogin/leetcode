"""
https://leetcode.com/problems/snapshot-array/
"""


from bisect import bisect_right


class SnapshotArray:
    """
    Store history for each item, then use binary search when getting
    the target snapped value.
    """

    def __init__(self, length: int):
        self.array = [[[-1, 0]] for _ in range(length)]
        self.currSnap = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.currSnap, val])

    def snap(self) -> int:
        self.currSnap += 1
        return self.currSnap - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect_right(self.array[index], [snap_id + 1]) - 1
        return self.array[index][i][1]
