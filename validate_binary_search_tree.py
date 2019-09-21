"""
https://leetcode.com/problems/validate-binary-search-tree/
"""

from test_helper import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        If we inorder traverse a BST, in other words, go through the tree from
        left -> root -> right, then each new visited node should have a greater
        value than the last node.

        And we use DFS to implement the inorder traverse.
        """
        workStack, currNode = [], root
        chkNum = None
        while workStack or currNode:
            while currNode:
                workStack.append(currNode)
                currNode = currNode.left

            currNode = workStack.pop()
            if chkNum is not None and currNode.val <= chkNum:
                return False

            chkNum = currNode.val
            currNode = currNode.right

        return True


givenDict = {
    5: (1, 4),
    4: (3, 6)
}
root = TreeNode(5)
root.create_tree(givenDict)
print(Solution().isValidBST(root))
