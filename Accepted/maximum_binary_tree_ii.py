"""
https://leetcode.com/problems/maximum-binary-tree-ii/
"""


from test_helper import TreeNode


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        """
        1. If no root, val will become the first root.
        2. If val is the largest value in the list, then since the val is the
            last item in the list, it means all the previous items will form
            its left child.
        3. If val is not the largest, it will always be added to the right
            sub tree of the current root, again, since it is the last item
            in the list.
        """
        if not root:
            return TreeNode(val)

        if root.val < val:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        root.right = self.insertIntoMaxTree(root.right, val)
        return root


root = TreeNode(5)
root.create_tree({
    5: (2, 4),
    2: (None, 1)
})
print(Solution().insertIntoMaxTree(root, 3))
