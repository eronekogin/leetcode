"""
https://leetcode.com/problems/range-module/
"""


from bisect import bisect_left, bisect_right


class RangeModule:
    """
    1. Take the ranges as a sorted list of numbers where the items on the
        even indexes stand for the openings of each range while the items on
        the odd indexes stand for the closings of each range. For example, if
        ranges = [10, 15, 20, 25], this covers the ranges of
        [10, 15) and [20, 25).

    2. When we want to add a range, let's say [14, 22), we do a binary search
        on the left most number in _ranges which is <= 14. In our case it is
        lb = bisect_left(ranges, left) = 1. And we also want to find the
        right most number in _ranges which is >= 22. In our case it is
        rb = bisect_right(ranges, right) = 3.

        2.1 If lb is odd, it means the left of the added range falls into an
            existing range.
            2.1.1 If rb is odd, it means the right of the added range falls
                into an existing range. This means the added range has
                connected the ranges specified by ranges[lb: rb], so we should
                collapse them by setting ranges[lb:rb] = []. In our case the
                ranges will become [10, 25] after addinng range [14, 22).
            2.1.2 If rb is even, it means the right of the added range does
                not fall into any existing range, so we need to create a new
                range by replacing ranges[lb: rb] to [right].
        2.2 If lb is even, it means the left of the added range does not fall
            into any existing range.
            2.2.1 If rb is odd, ranges[lb: rb] = [left].
            2.2.2 If rb is even, ranges[lb: rb] = [left, right].

    3. Similar cases happen as the above when we want to remove a range.

    4. When we want to query a target range [left, right), first we should find
        the right most boundary which is <= left and the left most boundary
        which is >= right.

        4.1 If lb == rb, it means there is no extra range between left and
            right.
        4.2 If lb is odd, it means the left side of the queried range falls
            into an existing range.

        So when both 4.1 and 4.2 are satisfied, it means the target range has
        been covered by the exisiting ranges.
    """

    def __init__(self):
        self._ranges = []

    def addRange(self, left: int, right: int) -> None:
        lb = bisect_left(self._ranges, left)
        rb = bisect_right(self._ranges, right)
        self._ranges[lb: rb] = [left] * (lb & 1 == 0) + [right] * (rb & 1 == 0)

    def queryRange(self, left: int, right: int) -> bool:
        lb = bisect_right(self._ranges, left)
        rb = bisect_left(self._ranges, right)
        return lb == rb and lb & 1

    def removeRange(self, left: int, right: int) -> None:
        lb = bisect_left(self._ranges, left)
        rb = bisect_right(self._ranges, right)
        self._ranges[lb: rb] = [left] * (lb & 1 == 1) + [right] * (rb & 1 == 1)
