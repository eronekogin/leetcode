"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
"""

from typing import List
from test_helper import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        Use the same idea as unique_binary_search_trees question.
        """
        def g(first: int, last: int) -> List[TreeNode]:
            rslt = []
            for root in range(first, last + 1):
                for leftNode in g(first, root - 1):
                    for rightNode in g(root + 1, last):
                        currNode = TreeNode(root)
                        currNode.left = leftNode
                        currNode.right = rightNode
                        rslt.append(currNode)

            return rslt or [None]  # Need to return [None] when rslt is empty.

        if not n:
            return []

        return g(1, n)


print(Solution().generateTrees(3))
