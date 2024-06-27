"""
https://leetcode.com/problems/booking-concert-tickets-in-groups/description/
"""


class Node:
    """
    Segment tree node
    """

    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None
        self.total = 0  # for range sum query
        self.mx = 0  # for range max query


class SegTree:
    """
    Segment tree
    """

    def __init__(self, start, end, val):

        def build(l, r):
            if l > r:
                return None
            if l == r:
                node = Node(l, r)
                node.total = val
                node.mx = val
                return node
            node = Node(l, r)
            m = (l + r) // 2
            node.left = build(l, m)
            node.right = build(m+1, r)
            node.mx = max(node.left.mx, node.right.mx)
            node.total = node.left.total + node.right.total
            return node

        self.root = build(start, end)

    def update(self, index, val):
        """
        update the total remain seats and the max remain seats for
        each node (range) in the segment tree
        """
        def update_helper(node):
            if node.s == node.e == index:
                node.total -= val
                node.mx -= val
                return
            m = (node.s + node.e) // 2
            if index <= m:
                update_helper(node.left)
            elif index > m:
                update_helper(node.right)
            node.mx = max(node.left.mx, node.right.mx)
            node.total = node.left.total + node.right.total
            return

        update_helper(self.root)

    def max_query(self, k, max_row, seats):
        """
        max query
        """
        def query_helper(node):
            if node.s == node.e:
                # check if the row number is less than maxRow and
                # the number of remains seats is greater or equal than k
                if node.e > max_row or node.total < k:
                    return []
                if node.e <= max_row and node.total >= k:
                    return [node.e, seats - node.total]

            # we want to greedily search the left subtree
            # to get the smallest row which has enough remain seats
            if node.left.mx >= k:
                return query_helper(node.left)

            return query_helper(node.right)

        return query_helper(self.root)

    def sum_query(self, end_row):
        """
        sum query
        """

        def query_helper(node, left, right):
            if left <= node.s and node.e <= right:
                return node.total

            m = (node.s + node.e) // 2

            if right <= m or left > m:
                return query_helper(node.left, left, right)

            return query_helper(node.left, left, m) + query_helper(node.right, m+1, right)

        return query_helper(self.root, 0, end_row)


class BookMyShow:
    """
    Book my show
    """

    def __init__(self, n: int, m: int):
        self.m = m
        self.seg = SegTree(0, n-1, m)
        # record the remain seats at each row
        self.seats = [m] * n
        # record the index of the smallest row that has remain seats > 0
        self.start_row = 0

    def gather(self, k: int, max_row: int) -> list[int]:
        """
        gather
        """
        res = self.seg.max_query(k, max_row, self.m)
        if res:
            row = res[0]
            self.seg.update(row, k)
            self.seats[row] -= k

        return res

    def scatter(self, k: int, max_row: int) -> bool:
        """
        scatter
        """
        if self.seg.sum_query(max_row) < k:
            return False

        i = self.start_row
        total = 0
        while total < k:
            prev_total = total
            total += self.seats[i]
            if total < k:
                # use up all the seats at ith row
                self.seg.update(i, self.seats[i])
                self.seats[i] = 0
                i += 1
                self.start_row = i
            elif total >= k:
                # occupy (k - prevTotal) seats at ith row
                self.seg.update(i, k - prev_total)
                self.seats[i] -= k - prev_total
        return True
