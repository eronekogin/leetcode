"""
https://leetcode.com/problems/recover-binary-search-tree/
"""

from test_helper import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Use Morris Traverse to inorder traverse the current BST so that the
        space cost could be reduced to O(1). Then for a BST with inorder
        traversal, a new visited node should be greater than the previous
        node and our goal is to find two incorrect nodes and exchange their
        value.

        Preasumption: Only two error nodes in the current BST.
        """
        if not root:  # Empty tree.
            return

        currNode, preNode = root, None
        errNodes = []
        while currNode:
            chkNode = None
            if not currNode.left:
                chkNode = currNode
                currNode = currNode.right
            else:
                # Try to find predecessor for the current node.
                node = currNode.left
                while node.right and node.right != currNode:
                    node = node.right

                if not node.right:
                    # Save the predecessor node to the right sub tree's right
                    # leaf node.
                    node.right = currNode
                    currNode = currNode.left
                else:  # leaf node stores the predecessor node.
                    node.right = None  # Recover tree shape.
                    chkNode = currNode
                    currNode = currNode.right

            if chkNode:
                if preNode and preNode.val > chkNode.val:
                    errNodes.append(preNode)
                    errNodes.append(chkNode)

                preNode = chkNode

        # Swap the value from the error nodes.
        if not errNodes:  # No errors found.
            return

        errNodes[0].val, errNodes[-1].val = errNodes[-1].val, errNodes[0].val


givenDict = {
    3: (1, 4),
    4: (2, None)
}
root = TreeNode(3)
root.create_tree(givenDict)
Solution().recoverTree(root)
