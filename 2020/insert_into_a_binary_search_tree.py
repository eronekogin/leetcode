"""
https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""


from test_helper import TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


root = TreeNode(4)
root.create_tree({
    4: (2, 7),
    2: (1, 3)
})
print(Solution().insertIntoBST(root, 5).print_tree())
