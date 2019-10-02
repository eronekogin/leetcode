"""
https://leetcode.com/problems/balanced-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        Use postorder traverse.
        """
        if not root:  # Empty tree.
            return True

        currNode, visitedNode, nodes = root, None, []
        depths = {}
        while nodes or currNode:
            while currNode:
                nodes.append(currNode)
                currNode = currNode.left  # Search the left sub tree first.

            currNode = nodes[-1]
            if not currNode.right or currNode.right == visitedNode:
                # Completed searching the right sub tree.
                currNode = nodes.pop()
                hl = depths.get(currNode.left, 0)
                hr = depths.get(currNode.right, 0)
                if abs(hl - hr) > 1:  # Delta height > 1.
                    return False

                # Store the height for the current node.
                depths[currNode] = 1 + max(hl, hr)
                visitedNode = currNode
                currNode = None
            else:
                currNode = currNode.right  # Then search the right sub tree.

        return True

    def isBalanced2(self, root: TreeNode) -> bool:
        """
        Use recursive solution.
        """
        if not root:  # Empty tree.
            return True

        hl = self.get_depth(root.left)
        hr = self.get_depth(root.right)
        if abs(hl - hr) > 1:
            return False

        return self.isBalanced2(root.left) and self.isBalanced2(root.right)

    def get_depth(self, root: TreeNode) -> int:
        if not root:  # Empty tree.
            return 0

        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))


givenDict = {
    3: (9, 20),
    20: (15, 7)
}
root = TreeNode(3)
root.create_tree(givenDict)
print(Solution().isBalanced2(root))
