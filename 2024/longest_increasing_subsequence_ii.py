"""
https://leetcode.com/problems/longest-increasing-subsequence-ii/description/
"""


class SegTree:
    """
    Segment tree
    """

    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n << 1)

    def query(self, l: int, r: int):
        """
        query max value between range l and r
        """
        l += self.n
        r += self.n
        rslt = 0
        while l < r:
            if l & 1:
                rslt = max(rslt, self.tree[l])
                l += 1

            if r & 1:
                r -= 1
                rslt = max(rslt, self.tree[r])

            l >>= 1
            r >>= 1

        return rslt

    def update(self, i: int, x: int):
        """
        update a node value
        """
        i += self.n
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i << 1], self.tree[(i << 1) + 1])


class Solution:
    """
    Solution
    """

    def length_of_lis(self, nums: list[int], k: int) -> int:
        """
        length of lis
        """
        rslt = 1
        st = SegTree(max(nums))

        for x in nums:
            x -= 1
            prev = st.query(max(0, x - k), x)
            rslt = max(rslt,  prev + 1)
            st.update(x, prev + 1)

        return rslt
