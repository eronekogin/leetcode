"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""


from test_helper import TreeNode


from typing import List
from collections import deque


class Solution:

    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        rslt, preLevel, queue = [root.val], 0, deque([(0, root)])
        while queue:
            currLevel, currNode = queue.popleft()
            if currLevel != preLevel:
                preLevel = currLevel
                rslt.append(currNode.val)

            rslt[-1] = max(rslt[-1], currNode.val)
            if currNode.left:
                queue.append((currLevel + 1, currNode.left))

            if currNode.right:
                queue.append((currLevel + 1, currNode.right))

        return rslt
