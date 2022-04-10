"""
https://leetcode.com/problems/add-one-row-to-tree/
"""


from test_helper import TreeNode


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """
        Traverse the original tree level by level.
        """
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot

        currNodes = [root]
        for _ in range(2, d):  # Get all the nodes on the d - 1 level.
            currNodes = [
                x
                for currNode in currNodes
                for x in (currNode.left, currNode.right)
                if x]

        for currNode in currNodes:
            left, right = currNode.left, currNode.right
            currNode.left = TreeNode(v)
            currNode.right = TreeNode(v)
            currNode.left.left = left
            currNode.right.right = right

        return root


root = TreeNode(4)
root.create_tree({
    4: (2, 6),
    2: (3, 1),
    6: (5, None)
})
print(Solution().addOneRow(root, 1, 2).print_tree())
