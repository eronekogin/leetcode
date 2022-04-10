"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""


from typing import List


from test_helper import NaryTreeNode


class Solution:
    def postorder(self, root: NaryTreeNode) -> List[int]:
        """
        Recursively.
        """
        if not root:
            return []

        rslt = []
        for child in root.children:
            rslt.extend(self.postorder(child))

        rslt.append(root.val)
        return rslt

    def postorder2(self, root: NaryTreeNode) -> List[int]:
        """
        Iteratively.
        """
        if not root:
            return []

        rslt, stack = [], [root]
        while stack:
            currNode = stack.pop()
            rslt.append(currNode.val)
            stack.extend(currNode.children)

        return rslt[::-1]
