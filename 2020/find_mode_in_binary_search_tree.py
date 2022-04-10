"""
https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""


from typing import List
from test_helper import TreeNode


class Solution:
    def __init__(self):
        self._currVal = None
        self._currFreq = self._maxFreq = 0
        self._rslt = []

    def _inorder_traverse(
            self, root: TreeNode, countFreq: bool = False) -> None:
        if not root:
            return

        self._inorder_traverse(root.left, countFreq)

        if self._currVal != root.val:
            self._currVal = root.val
            self._currFreq = 0

        self._currFreq += 1
        if countFreq:
            self._maxFreq = max(self._maxFreq, self._currFreq)
        elif self._currFreq == self._maxFreq:
            self._rslt.append(self._currVal)

        self._inorder_traverse(root.right, countFreq)

    def findMode(self, root: TreeNode) -> List[int]:
        """
        1. Inorder traverse the tree to count the maximum frequency and how
            many items has that frequency.
        2. Then inorder traverse the tree again to collect those items having
            maximum frequency.
        """
        self._inorder_traverse(root, True)
        self._currVal, self._currFreq = None, 0
        self._inorder_traverse(root)
        return self._rslt
