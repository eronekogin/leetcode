"""
https://leetcode.com/problems/complete-binary-tree-inserter/
"""


from test_helper import TreeNode


class CBTInserter:

    def __init__(self, root: TreeNode):
        currParents = [root]
        currLeaves = [node for node in [root.left, root.right] if node]
        while len(currLeaves) == (len(currParents) << 1):
            currParents = currLeaves
            currLeaves = [
                node
                for parent in currParents
                for node in [parent.left, parent.right]
                if node
            ]

        self.root = root
        self.currParents = currParents
        self.currLeaves = currLeaves

    def insert(self, v: int) -> int:
        if len(self.currLeaves) == (len(self.currParents) << 1):
            self.currParents = self.currLeaves
            self.currLeaves = []

        parent = self.currParents[len(self.currLeaves) >> 1]
        if parent.left:
            parent.right = TreeNode(v)
            self.currLeaves.append(parent.right)
        else:
            parent.left = TreeNode(v)
            self.currLeaves.append(parent.left)

        return parent.val

    def get_root(self) -> TreeNode:
        return self.root
