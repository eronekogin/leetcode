"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

from test_helper import TreeNode
from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """ 
        Inorder traversal means to go through all the root's left sub tree 
        first with inorder, then to the root node, then to go through all 
        the right sub tree with inorder. 

        Use DFS for this solution and it is a perfect scenario to use stack.
        """
        workStack, rslt, currNode = [], [], root
        while workStack or currNode:
            while currNode:
                workStack.append(currNode)
                currNode = currNode.left  # Search left sub tree first.

            currNode = workStack.pop()
            rslt.append(currNode.val)
            currNode = currNode.right  # Then to the right sub tree.

        return rslt


root = TreeNode(1)
givenDict = {
    1: (2, 3),
    2: (4, 5),
    3: (6, 7),
    4: (8, None),
    8: (None, 10),
    10: (11, 12),
    6: (None, 9)
}
root.create_tree(givenDict)
print(Solution().inorderTraversal(root))
