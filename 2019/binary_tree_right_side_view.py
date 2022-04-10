"""
https://leetcode.com/problems/binary-tree-right-side-view/
"""


from test_helper import TreeNode
from typing import List
from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:  # Empty tree.
            return []

        rightMostNodes = {}  # level: value
        queue = deque([(root, 0)])
        while queue:
            currNode, level = queue.popleft()
            rightMostNodes[level] = currNode.val
            if currNode.left:
                queue.append((currNode.left, level + 1))

            if currNode.right:
                queue.append((currNode.right, level + 1))

        return [rightMostNodes[l] for l in range(level + 1)]
