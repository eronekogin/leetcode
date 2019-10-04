"""
https://leetcode.com/problems/path-sum/
"""


from test_helper import TreeNode


class Solution:
    def hasPathSum2(self, root: TreeNode, target: int) -> bool:
        """
        Use level order traverse.
        """
        if not root:
            return False

        nodes = [(root, target)]
        while nodes:
            nextNodes = []
            for node, value in nodes:
                if not node.left and not node.right and node.val == value:
                    return True  # Arrived at a leaf node.

                if node.left:
                    nextNodes.append((node.left, value - node.val))

                if node.right:
                    nextNodes.append((node.right, value - node.val))

            nodes = nextNodes

        return False

    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:  # Empty tree.
            return False

        if not root.left and not root.right:  # Leaf node.
            return root.val == target

        return self.hasPathSum(root.left, target - root.val) or \
            self.hasPathSum(root.right, target - root.val)
