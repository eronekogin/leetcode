"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""


from typing import List


from test_helper import NaryTreeNode


class Solution:
    def preorder(self, root: NaryTreeNode) -> List[int]:
        """
        Use iteration.
        """
        stack, rslt = root and [root], []
        while stack:
            currNode = stack.pop()
            rslt.append(currNode.val)
            stack.extend(reversed(currNode.children or []))

        return rslt

    def preorder2(self, root: NaryTreeNode) -> List[int]:
        """
        Use recursion.
        """
        rslt = []
        if root:
            rslt.append(root.val)
            for child in root.children:
                rslt.extend(self.preorder2(child))

        return rslt
