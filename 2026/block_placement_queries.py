"""
https://leetcode.com/problems/block-placement-queries/description/
"""

from sortedcontainers import SortedList


class SegmentTree:
    """
    Segment Tree
    """

    def __init__(self, mx: int) -> None:
        # each item i in self.seg contains the gap size
        # that ends at i.
        self.seg = [0] * (mx << 2)
        self.mx = mx

    def update(self, i: int, v: int, p: int, l: int, r: int):
        """
        add a new value
        """
        if l == r:
            self.seg[p] = v
            return

        m = l + ((r - l) >> 1)
        if i <= m:
            self.update(i, v, p << 1, l, m)
        else:
            self.update(i, v, (p << 1) | 1, m + 1, r)

        self.seg[p] = max(self.seg[p << 1], self.seg[(p << 1) | 1])

    def query(self, start: int, end: int, p: int, l: int, r: int) -> int:
        """
        query a range
        """
        if start <= l and r <= end:
            return self.seg[p]

        m = l + ((r - l) >> 1)
        rslt = 0
        if start <= m:
            rslt = max(rslt, self.query(start, end, p << 1, l, m))

        if end > m:
            rslt = max(rslt, self.query(start, end, (p << 1) | 1, m + 1, r))

        return rslt


class Solution:
    """
    Solution
    """

    def get_results(self, queries: list[list[int]]) -> list[bool]:
        """
        get results
        """
        mx = 50000
        st = SegmentTree(mx)
        sl = SortedList([0, mx])

        st.update(mx, mx, 1, 0, mx)
        rslt: list[bool] = []

        for q in queries:
            if q[0] == 1:
                x = q[1]
                i = min(len(sl) - 1, sl.bisect_right(x))
                r = sl[i]
                l = sl[i - 1] if i > 0 else sl[0]
                st.update(x, x - l, 1, 0, mx)
                st.update(r, r - x, 1, 0, mx)
                sl.add(x)
            else:
                x = q[1]
                sz = q[2]
                i = min(len(sl) - 1, sl.bisect_right(x))
                prev = sl[0] if i == 0 else sl[i - 1]
                mx_space = max(
                    x - prev,
                    st.query(0, prev, 1, 0, mx)
                )
                rslt.append(mx_space >= sz)

        return rslt
