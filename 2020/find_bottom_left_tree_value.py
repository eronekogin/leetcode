"""
https://leetcode.com/problems/find-bottom-left-tree-value/
"""


from test_helper import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        Traverse the tree level by level until there is no new level. Then the
        current level's first node is our target.
        """
        currNodes = [root]
        while currNodes:
            nextNodes = []
            for node in currNodes:
                if node.left:
                    nextNodes.append(node.left)

                if node.right:
                    nextNodes.append(node.right)

            if not nextNodes:
                return currNodes[0].val

            currNodes = nextNodes
