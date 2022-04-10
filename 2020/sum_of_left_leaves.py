"""
https://leetcode.com/problems/sum-of-left-leaves/
"""


from test_helper import TreeNode
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, 0)])
        rslt = 0
        while queue:
            curr, isLeft = queue.popleft()
            if isLeft and not curr.left and not curr.right:
                # Found a leaf node.
                rslt += curr.val
                continue

            if curr.left:
                queue.append((curr.left, 1))

            if curr.right:
                queue.append((curr.right, 0))

        return rslt
