"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""


from test_helper import NaryTreeNode
from typing import List
from collections import deque


class Solution:
    def levelOrder(self, root: NaryTreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(0, root)])
        preLevel = 0
        rslt = [[]]
        while queue:
            level, curr = queue.popleft()
            if level != preLevel:
                rslt.append([])
                preLevel = level

            rslt[-1].append(curr.val)
            level += 1
            for node in curr.children or []:
                queue.append((level, node))

        return rslt


n3 = NaryTreeNode(3, [NaryTreeNode(5), NaryTreeNode(6)])
root = NaryTreeNode(1, [n3, NaryTreeNode(2), NaryTreeNode(4)])
print(Solution().levelOrder(root))
