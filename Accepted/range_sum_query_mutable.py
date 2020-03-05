"""
https://leetcode.com/problems/range-sum-query-mutable/
"""


from typing import List


class SegmentTreeNode():
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):

        def create_tree(start: int, end: int) -> SegmentTreeNode:
            if start > end:
                return None

            currNode = SegmentTreeNode(start, end)

            if start == end:  # Reach leaf node.
                currNode.total = nums[start]
            else:
                mid = start + ((end - start) >> 1)  # (start + end) // 2.
                currNode.left = create_tree(start, mid)
                currNode.right = create_tree(mid + 1, end)
                currNode.total = currNode.left.total + currNode.right.total

            return currNode

        # Create a segment tree from the input list.
        self.root = create_tree(0, len(nums) - 1)

    def update(self, i: int, val: int):

        def update_tree(currNode: SegmentTreeNode, i: int, val: int):
            if currNode.start == currNode.end:  # Reach leaf node.
                currNode.total = val
            else:
                mid = currNode.start + ((currNode.end - currNode.start) >> 1)
                if i <= mid:
                    update_tree(currNode.left, i, val)
                else:
                    update_tree(currNode.right, i, val)

                currNode.total = currNode.left.total + currNode.right.total

        # Update the segment tree.
        update_tree(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:

        def sum_tree(currNode: SegmentTreeNode, start: int, end: int) -> int:
            if currNode.start == start and currNode.end == end:
                return currNode.total

            mid = currNode.start + ((currNode.end - currNode.start) >> 1)
            if end <= mid:  # On the left side.
                return sum_tree(currNode.left, start, end)
            elif start >= mid + 1:  # On the right side.
                return sum_tree(currNode.right, start, end)
            else:  # Between.
                return sum_tree(currNode.left, start, mid) + sum_tree(
                    currNode.right, mid + 1, end)

        return sum_tree(self.root, i, j)


n = NumArray([0, 9, 5, 7, 3])
print(n.sumRange(1, 2))
