"""
https://leetcode.com/problems/count-complete-tree-nodes/
"""


from test_helper import TreeNode


class Solution:
    def get_height(self, root: TreeNode) -> int:
        if not root:
            return 0

        currNode, height = root, 0
        while currNode:
            height += 1
            currNode = currNode.left

        return height

    def countNodes(self, root: TreeNode) -> int:
        """
        A complete binary tree could be:

        1. The left sub tree is a perfect binary tree 
            while the right sub tree is a complete binary tree.
        2. The left sub tree is a complete binary tree
            while the right sub tree is a perfect binary tree.

        For a perfect binary tree, if its height is h, the total nodes
        it has is 2^0 + 2^1 + ... + 2^(h - 1) = 2^0 * (1 - 2^h) / (1 - 2)
        = 2^h - 1. 
        """
        nodeCnt, currNode, rootHeight = 0, root, self.get_height(root)
        while currNode:
            leftHeight = rootHeight - 1
            rightHeight = self.get_height(currNode.right)
            if leftHeight == rightHeight:
                # The left sub tree is a perfect binary tree.
                # So the total nodes in root and its left sub tree is:
                # 1 + 2 ^ h - 1 = 2 ^ h.
                nodeCnt += 1 << leftHeight
                currNode = currNode.right
            else:
                # The right sub tree is a perfect binary tree.
                # So the total nodes in root and its right sub tree is:
                # 1 + 2 ^ h - 1 = 2 ^ h.
                nodeCnt += 1 << rightHeight
                currNode = currNode.left

            rootHeight -= 1

        return nodeCnt


root = TreeNode(1)
root.create_tree({
    1: (2, 3),
    2: (4, 5),
    3: (6, None)
})
print(Solution().countNodes(root))
